#!/usr/bin/env python3

import json
import xmltodict
import logging
import socket
import sys
import argparse
import os
from Bio import SeqIO

# -------------------------
# global variables
# -------------------------

OUTPUT_FILE = "filtered_fastq_output.fastq"

# -------------------------
# arg parser for file names and logging setting
# -------------------------
parser = argparse.ArgumentParser(description='Generates a summary json from an input mmCIF file')
parser.add_argument(
    '-l', '--loglevel',
    required=False,
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    default='WARNING',
    help='Set the logging level (default: WARNING)'
)
parser.add_argument(
    '-f', '--fastqfile',
    type=str,
    required=True,
    help='The path to the input fastq file'
)
parser.add_argument(
    '-e', '--encoding',
    choices=['fastq-sanger', 'fastq-solexa', 'fastq-illumina'],
    default='fastq-sanger',
    help='The FASTQ encoding format (default: fastq-sanger)'
)
parser.add_argument(
    '-t', '--threshold',
    type=int,
    default=30,
    help='The minimum average phred score for a sequence to be saved (default: 30)'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    default=OUTPUT_FILE,
    help=f'The path to the output FASTQ file (default: {OUTPUT_FILE})'
)
args = parser.parse_args()

format_string = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(module)s.%(funcName)s:%(lineno)s - %(levelname)s - %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_string)


# -------------------------
# Functions
# -------------------------
def load_fastq(input_file: str, encoding: str, threshold: int) -> list:
    """
    Opens the FASTQ file and generates the average phred score for each entry,
    if the average phred is above the threshold the read will be appened to a saved list

    Args:
        input_file: The path to the FASTQ file
        encoding: The FASTQ encoding method of the phred scores
                  (options: fastq-sanger, fastq-solexa, fastq-illumina)
        threshold: The minimum average phred score to be saved

    Returns:
        reads_filter: The reads with average phred scores above the given threshold
    """
    reads_filter = []
    try:
        logging.debug(f"About to read {input_file}")
        with open(input_file, "r") as f:
            logging.info(f"Parsing {input_file} with {encoding} encoding")
            for record in SeqIO.parse(f, encoding):
                avg_phred = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
                if avg_phred >= threshold:
                    reads_filter.append(record)
            logging.info(
                f"Sucessfully found {len(reads_filter)} sequences that " +
                "had a avg phred above {threshold}"
                )
        return reads_filter
    except FileNotFoundError:
        logging.error(f"Could not read {input_file}, terminating program.")
        sys.exit(1)
    

def create_filtered_file(output_file: str, reads_filter: list, encoding: str):
    """
    Creates a FASTQ file based on a list of FASTQ reads.

    Args:
        output_file: The path of the outputfile
        reads_filter: The list of reads to be output
        encoding: The FASTQ encoding method of the phred scores
                  (options: fastq-sanger, fastq-solexa, fastq-illumina)

    Returns:
    """
    try:
        logging.debug(f"About to write to {output_file}")
        with open(output_file, "w") as out:
            logging.info(f"Writing to {output_file} with {encoding} encoding")
            SeqIO.write(reads_filter, out, encoding)
    except FileNotFoundError:
        with open(OUTPUT_FILE, "w") as out:
            logging.info(
                f"Could not write to {output_file}, "
                "writing to {OUTPUT_FILE} with {encoding} encoding"
                )
            SeqIO.write(reads_filter, out, encoding)


def main():
    logging.info("Starting fastq_filter program")
    reads_filter = load_fastq(args.fastqfile, args.encoding, args.threshold)
    create_filtered_file(args.output, reads_filter, args.encoding)
    logging.info("Successfully Completed Workflow!")

if __name__ == "__main__":
    main()

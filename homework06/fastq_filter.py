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

OUTPUT_FILE = "filtered_fastq_output.json"

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
    default=30
    help='The minimum average phred score for a sequence to be saved (default: 30)'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    default=OUTPUT_JSON,
    help=f'The path to the output JSON file (default: {OUTPUT_JSON})'
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
    with open(input_file, "r") as f
        for record in SeqIO.parse(f, encoding):
            avg_phred = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
            if avg_phred >= threshold:
                reads_filter.append(record)
    return reads_filter
    

def create_filtered_file(output_file: str, reads_filter: list, encoding: str)
    """
    Creates a FASTQ file based on a list of FASTQ reads.

    Args:
        output_file: The path of the outputfile
        reads_filter: The list of reads to be output
        encoding: The FASTQ encoding method of the phred scores
                  (options: fastq-sanger, fastq-solexa, fastq-illumina)

    Returns:
    """
    with open(output_file, "w") as out:
        SeqIO.write(reads_filter, out, encoding)


def main():
    reads_filter = load_fastq(args.fastqfile, args.encoding, args.threshold)
    create_filtered_file(args.output, reads_filter, args.encoding)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from Bio.SeqIO.FastaIO import SimpleFastaParser
import logging
import socket
import sys
import argparse
import os

# -------------------------
# global variables
# -------------------------

OUTPUT_FILE = "output.fasta"

# -------------------------
# Logging setup
# -------------------------
parser = argparse.ArgumentParser(description='Summarize FASTQ file and output JSON summary')
parser.add_argument(
    '-l', '--loglevel',
    required=False,
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    default='WARNING',
    help='Set the logging level (default: WARNING)'
)
parser.add_argument(
    '-f', '--fastafile',
    type=str,
    required=True,
    help='The path to the input FASTA file'
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
def open_input_fasta(input_file: str) -> list[dict]:
    """
    Converts a given FASTA file into a list of dictionaries

    Args:
        input_file: The path to a FASTA file that is to be opened and 
                    converted to a list of dicts 

    Returns:
        sequences: A list of dictionaries of:
                    + headers
                    + sequences
                    + lengths 
                    from the given FASTA file
    """
    sequences = []
    logging.debug(f"About to open {input_file}")
    try:
        with open(input_file, "r") as f:
            logging.info(f"opening {input_file}")
            for header, sequence in SimpleFastaParser(f):
                entry = {
                    "header" : header,
                    "sequence" : sequence,
                    "length": len(sequence)
                    }
                sequences.append(entry)
        logging.info(f"Finished parsing through {input_file}, with {len(sequence)} sequences")
        return sequences
    except FileNotFoundError:
        logging.error(f"Could not open {input_file}, program terminating.")
        sys.exit(1)


def write_output_fasta(output_file: str, sequences: list):
    """
    Writes a FASTA file from a list of formatted dictionaries

    Args:
        output_file: The path to the output_file
        sequences: The list of dictionary entries that will 
                    be made into the FASTA file

    Returns:
    """
    try:
        logging.debug(f"About to write to {output_file}")
        with open(output_file, "w") as out:
            loggin.info(f"Writing to {output_file}")
            written_count = 0
            for entry in sequences:
                if entry["length"] > 1000:
                    out.write(f">{entry["header"]}\n")
                    out.write(f"{entry["sequence"]}\n")
                    written_count += 1
            logging.info(f"Successfully written {written_count} sequences, 
                            which have length > 1,000")
    except FileNotFoundError:
        log.info(f"could not find path to {output_file}, writing to {OUTPUT_FILE}")
        with open(OUTPUT_FILE, "w") as out:
            written_count = 0
            for entry in sequences:
                if entry["length"] > 1000:
                    out.write(f">{entry["header"]}\n")
                    out.write(f"{entry["sequence"]}\n")
                    written_count += 1
             logging.info(f"Successfully written {written_count} sequences, 
                            which have length > 1,000")


def main():
    logging.debug("Beginning fasta_filter program")
    sequences = open_input_fasta(args.fastafile)
    write_output(args.output, sequences)
    logging.info("Successfully Completed Workflow!")


if __name__ == "__main__":
    main()
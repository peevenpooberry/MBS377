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
    with open(input_file, "r") as f:
        for header, sequence in SimpleFastaParser(f):
            entry = {
                "header" : header,
                "sequence" : sequence,
                "length": len(sequence)
                }
            sequences.append(entry)
    return sequences


def write_output_fasta(output_file: str, sequences: list):
    """
    Writes a FASTA file from a list of formatted dictionaries

    Args:
        output_file: The path to the output_file
        sequences: The list of dictionary entries that will 
                    be made into the FASTA file

    Returns:
    """
    with open(output_file, "w") as out:
        for entry in sequences:
            if entry["length"] > 1000:
                out.write(f">{entry["header"]}\n")
                out.write(f"{entry["sequence"]}\n")


def main():
    sequences = open_input_fasta(args.fastafile)
    write_output(args.output, sequences)


if __name__ == "__main__":
    main()
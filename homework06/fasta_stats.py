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

OUTPUT_FILE = "output_fasta_summary.json"

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
def read_file(input_file: str) -> list[dict]:
    """
    Opens and parses through a given FASTA file, and creates a list of dictionaries, 
    containing each sequence's id and length

    Args:
        input_file: The path to the FASTA file to be read

    Returns:
        sequences: A list of dictionaries for each sequence, containing:
                    + id
                    + length
    """
    sequences = []
    try:
        logging.debug(f"About to read {input_file}")
        with open(input_file, "r") as f:
            logging.info(f"Parsing {input_file}")
            for header, sequence in SimpleFastaParser(f):
                #("Header", "Sequence")
                parts = header.split("|")
                entry = {
                    "id": parts[1],
                    "length": len(sequence)
                    }
                sequences.append(entry)
            logging.info(f"Successfully parsed {len(sequence)} reads")
        return sequences
    except FileNotFoundError:
        logging.error(f"Could not read {input_file}, terminating program.")
        sys.exit(1)


def make_summary(output_file: str, sequences: list)
    """
    Creates a summary text file based on id and lengths contained in the list of dictionaries
    by sequence

    Args:
        output_file: The path to the output file 
        sequences: A list of dictionaries with each sequence having an id and sequence length

    Returns:
    """
    logging.debug(f"About to write to {output_file}")
    with open(output_file, "w") as out:
        logging.info(f"Writing stats in {output_file}")
        out.write(f"Num Sequences: {len(sequences)}\n")

        total_res = 0
        for entry in sequences:
            total_res += entry["length"]
        out.write(f"Total Residues: {total_res}\n")

        sorted_seq = sorted(sequences, key=lambda x : x["length"], reverse=True)
        out.write(f"Longest Accession: {sorted_seq[0]["id"]} ({sorted_seq[0]["length"]} residues)\n")
        out.write(f"Shortest Accession: {sorted_seq[-1]["id"]} ({sorted_seq[-1]["length"]} residues)")
        logging.info("Completed writing stats")


def main():
    logging.info("Beginning fasta_stats program")
    sequences = read_file(args.fastafile)
    make_summary(args.output, sequences)
    logging.info("Successfully Completed Workflow!")
    

if __name__ == "__main__":
    main()

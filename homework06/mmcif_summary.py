#!/usr/bin/env python3

from Bio.PDB.MMCIFParser import MMCIFParser
import argparse
import logging
import socket
import sys
import json
import os

# -------------------------
# global variables
# -------------------------

OUTPUT_FILE = "output_mmcif_summary.json"

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
    '-f', '--mmcif',
    type=str,
    required=True,
    help='The path to the input mmcif file'
)

parser.add_argument(
    '-o', '--output',
    type=str,
    default=OUTPUT_FILE,
    help=f'The path to the output JSON file (default: {OUTPUT_FILE})'
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
def open_input_file(input_file: str) -> 'Bio.PDB.Structure.Structure':
    """
    Opens the given input mmCIF file and converts it to a Structure class from Bio.PDB.MMCIFParser 
    via parser.

    Args:
        input_file: str, the input mmCIF file to be summarized

    Returns:
        structure: Structure, the file formatted by the Bio.PDB.MMCIFParser
    """
    logging.debug("About to open main file")
    parser = MMCIFParser()
    try:
        with open(input_file, "r") as f:
            structure = parser.get_structure("", f)
            logging.info(f"Successfully opened {input_file}")
        return structure
    except FileNotFoundError:
        logging.error(f"{input_file} not found, ending process")
        sys.exit(1)


def parse_file(structure:'Bio.PDB.Structure.Structure')-> list[dict]:
    """
    Iterates through the MMCIF.Parser and returns a summary about the chains within.

    Args:
        structure: Structure, the file formatted by the Bio.PDB.MMCIFParser

    Returns:
        summary: list[dict], a list of entries of chain summaries of dicts containing:
            "chain_id": str
            "total_residues": int
            "standard_residues": int
            "hetero_residues": int
    """
    summary = []

    logging.info("Beginning to parse file")
    for model in structure:
        for chain in model:
            new_entry = {"chain_id": None,
            "total_residues": None,
            "standard_residues": None,
            "hetero_residues": None
            }
            chain_id = chain.id
            total_residues = len(chain)
            res_count = 0
            hetero_count = 0
            
            logging.debug(f"Parsing chain {chain_id}")
            for residue in chain:
                id = residue.get_id()
                hetfield = id[0]
                if hetfield == " ":
                    res_count += 1
                else:
                    hetero_count += 1
            logging.debug(f"Finished parsing chain {chain_id}")
            new_entry["chain_id"] = chain_id
            new_entry["total_residues"] = total_residues
            new_entry["standard_residues"] = res_count
            new_entry["hetero_residues"] = hetero_count
            summary.append(new_entry)
    
    logging.info(f"Finished parsing with {len(summary)} chains")
    return summary 


def generate_output_file(output_file: str, summary: list[dict]):
    """
    Description.

    Args:
        output_file: str, The name of the output json file.
        summary: list[dict], a list of entries of chain summaries of dicts containing:
            "chain_id": str
            "total_residues": int
            "standard_residues": int
            "hetero_residues": int

    Returns:
        result
    """
    logging.info(f"Writing to {output_file}")
    wrapper = {"chains": summary}
    with open(output_file, 'w') as outfile:
        logging.debug(f"Loading to {output_file}")
        try:
            json.dump(wrapper, outfile, indent=2)
        except Exception as e:
            logging.error(f"Writing to {output_file} failed:\n{e}")


def main():
    logging.info("Beginning mmCIF Summary workflow")
    structure = open_input_file(args.mmcif)
    summary = parse_file(structure)
    generate_output_file(args.output, summary)
    logging.info("mmCIF Summary workflow is complete!")


if __name__ == "__main__":
    main()

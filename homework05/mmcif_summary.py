from Bio.PDB.MMCIFParser import MMCIFParser
import argparse
import logging
import socket
import sys
import json
import os

# -------------------------
# Constants (configuration)
# -------------------------
INPUT_FILE = "4HHB.cif"
OUTPUT_FILE = "4HHB_summary.json"

# -------------------------
# Logging (configuration)
# -------------------------
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--loglevel',
                    type=str,
                    required=False,
                    default='WARNING',
                    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL')

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

args = parser.parse_args()
logging.basicConfig(level=args.loglevel, format=format_str)

# -------------------------
# Functions
# -------------------------
def open_input_file(INPUT_FILE: str) -> 'Bio.PDB.Structure.Structure':
    """
    Opens the given input mmCIF file and converts it to a Structure class from Bio.PDB.MMCIFParser 
    via parser.

    Args:
        INPUT_FILE: str, the input mmCIF file to be summarized

    Returns:
        structure: Structure, the file formatted by the Bio.PDB.MMCIFParser
    """
    logging.debug("About to open main file")
    parser = MMCIFParser()
    try:
        with open(INPUT_FILE, "r") as f:
            structure = parser.get_structure("", f)
            logging.info(f"Successfully opened {INPUT_FILE}")
        return structure
    except FileNotFoundError:
        logging.error(f"{INPUT_FILE} not found, ending process")
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
    
    logging.info(f"Finished parsing {INPUT_FILE} has {len(summary)} chains")
    return summary 


def generate_output_file(OUTPUT_FILE="Output.json": str, summary: list[dict]):
    """
    Description.

    Args:
        OUTPUT_FILE: str, The name of the output json file.
        summary: list[dict], a list of entries of chain summaries of dicts containing:
            "chain_id": str
            "total_residues": int
            "standard_residues": int
            "hetero_residues": int

    Returns:
        result
    """
    logging.info(f"Writing to {OUTPUT_FILE}")
    try:
        full_path = os.path.join("output_files", OUTPUT_FILE)
    except:
        logging.debug("Missing output directory")
        full_path = OUTPUT_FILE
    finally:
        wrapper = {"chains": summary}
        with open(full_path, 'w') as outfile:
            logging.debug(f"Loading to {OUTPUT_FILE}")
            try:
                json.dump(wrapper, outfile, indent=2)
            except Exception as e:
                logging.error(f"Writing to {OUTPUT_FILE} failed:\n{e}")


def main():
    logging.info("Beginning mmCIF Summary workflow")
    structure = open_input_file(INPUT_FILE)
    summary = parse_file(structure)
    generate_output_file(OUTPUT_FILE, summary)
    logging.info("mmCIF Summary workflow is complete!")


if __name__ == "__main__":
    main()

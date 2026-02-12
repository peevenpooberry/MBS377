from Bio.PDB.MMCIFParser import MMCIFParser
import argparse
import logging
import socket
import sys
import json

# -------------------------
# Constants (configuration)
# -------------------------
INPUT_FILE = ""
OUTPUT_FILE = ""

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
def open_input_file(INPUT_FILE: str)-> Structure:
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
            try:
                structure = parser.get_structure("", f)
            except Exception as e:
                logging.error(f"Incorrect input file format provided!\n{e}")
                sys.exit(1)
            
            logging.info("Successfully opened input file")
        return structure
    except FileNotFoundError:
        logging.error("Input file not found, ending process")
        sys.exit(1)


def parse_file(structure: Structure)-> list[dict]:
    """
    Iterates through the MMCIF.Parser and returns a summary about the chains within.

    Args:
        structure: Structure, the file formatted by the Bio.PDB.MMCIFParser

    Returns:
        chains: list[dict], a list of entries of chain summaries of dicts containing:
            "chain_id": str
            "total_residues": int
            "standard_residues": int
            "hetero_residues": int
    """
    chains = []

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
                hetfield = id[0]
                if hetfield == "":
                    res_count += 1
                else:
                    hetero_count += 1
            logging.debug(f"Finished parsing chain {chain_id}")
            new_entry["chain_id"] = chain_id
            new_entry["total_residues"] = total_residues
            new_entry["standard_residues"] = res_count
            new_entry["hetero_residues"] = hetero_count
            chains.append(new_entry)
    
    logging.info(f"Finished parsing {Input_File} have {len(chains)} chains")
    return chains  


def generate_output_file(OUTPUT_FILE: str, data: list[dict]):
    """
    Description.

    Args:
        OUTPUT_FILE: str, The name of the output json file.
        data: list[dict], a list of entries of chain summaries of dicts containing:
            "chain_id": str
            "total_residues": int
            "standard_residues": int
            "hetero_residues": int

    Returns:
        result
    """
    logging.info(f"Writing to {OUTPUT_FILE}")
    try:
        full_path = os.path.join(output_files, OUTPUT_FILE)
    except:
        logging.debug("Missing output directory")
        full_path = OUTPUT_FILE
    finally:
        wrapper = {"chains": data}
            with open(full_path, 'w') as outfile:
                logging.debug(f"Loading to {OUTPUT_FILE}")
                try:
                    json.dump(summary.model_dump(), outfile, indent=2)
                except Exception as e:
                    logging.error(f"Writing to {OUTPUT_FILE} failed:\n{e}")


def main():
    logging.info("Beginning mmCIF Summary workflow")
    structure = open_input_file(INPUT_FILE)
    data = parse_file(structure)
    generate_output_file(OUTPUT_FILE, data)
    logging.info("mmCIF Summary workflow is complete!")


if __name__ == "__main__":
    main()
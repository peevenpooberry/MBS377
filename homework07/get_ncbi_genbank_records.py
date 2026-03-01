#!/usr/bin/env python3

from Bio import Entrez, SeqIO
import redis
import os
import sys
import socket
import json
import logging
import argparse

# -------------------------
# global variables
# -------------------------

SEARCH_TERM = "Arabidopsis thaliana AND AT5G10140"
ENTREZ_EMAIL = "Random@example.com"
OUTPUT_FILE = "records.txt"

# -------------------------
# Logging setup
# -------------------------
parser = argparse.ArgumentParser(description='Sends API call to NCBI protein db and creates ' + 
                                 'an output file with the top results')
parser.add_argument(
    '-l', '--loglevel',
    required=False,
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    default='WARNING',
    help='Set the logging level (default: WARNING)'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    default=OUTPUT_FILE,
    help=f'The name of the output file (default: {OUTPUT_FILE})'
)
parser.add_argument(
    '-s', '-search',
    default=SEARCH_TERM,
    help=(
        'The search terms the user wishes to get from the NCBI protein db API ' +
        f'(default: {SEARCH_TERM})'
    ),
    type=str
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
def get_gbID_num(search_term: str, entrez_email=ENTREZ_EMAIL, retmax=30)-> list[str]:
    """
    Gets all the top results from a API request to the NCIB protein database using a given search term

    Args:
        search_term: A string that will be used to get a request
            - default: "Arabidopsis thaliana AND AT5G10140"
            - can be changed using `-s` flag when running program in console
        entrez_email: A string in the format of an email that will be used for the API request
            - Not necessary to change
            - default: "Random@example.com"
            - can be changed by altering global variable ENTREZ_EMAIL
        retmax: An int that is the amount of results which are returned
            - default: 30
    """
    logging.info(f"Getting IDs for the search {search_term}")
    Entrez.email = entrez_email
    with Entrez.esearch(db="protein", term=search_term, retmax=retmax) as h:
        results = Entrez.read(h)
        gbID = results["IdList"]
        logging.debug("Finished get_ID_num()")
        return gbID


def list_to_str(input: list[str])-> str:
    """
    Turns a list of strings into a long string of the elements separated by commas
    ex. ["a", "b", "c"] -> "a, b, c"

    Args:
        input: A list of strings
    
    Returns:
        output: A long string of the input elements separated by commas
    """
    logging.debug("Starting list_to_str()")
    output = ""
    for index, elem in enumerate(input):
        if index == len(input) - 1:
            output += f"{elem}"
        else:
            output += f"{elem}, "
    logging.debug("Finished list_to_str()")
    return output


def get_record(gbID: list[str])-> list['Bio.SeqRecord.SeqRecord']:
    """
    Given a list of NCIB Protein Database IDs, returns a list of matching Bio.Seq records

    Args:
        gbID: A list of IDs as strings
    
    Returns:
        rec_list: A list of Bio.Seq records
    """
    logging.info("Getting records")
    gbID_str = list_to_str(gbID)
    with Entrez.efetch(db="protein", id=gbID_str, rettype="gb", retmode="text") as h:
        record = SeqIO.parse(h, "gb")
        rec_lst = list(record)
        logging.debug("Finished get_record()")
        return rec_lst


def store_records(rec_lst: list['Bio.SeqRecord.SeqRecord'], db=0):
    """
    Stores a list of Bio.Seq records to a locally hosted Redis databse in the form of
    {ID: json string of (ID, Name, Description, Sequence)}

    Args:
        rec_lst: A list of Bio.Seq records
        db: An optional int type input that will create or specify a Redis database
            - default: 0
    
    Returns
        None: Will create/append entries to a Redis database consisting of 
            - key: ID
            - value: json string of
                "ID": ID of record
                "Name": Name of record
                "Description": Description of record
                "Sequence": Sequence of record
    """
    logging.info("Starting store_records()")
    try:
        rd = redis.Redis(host="127.0.0.1", port=6379, db=db)
        for record in rec_lst:
            entry = {
                "ID": record.id, 
                "Name": record.name,
                "Description": record.description,
                "Sequence": str(record.seq)
            }
            logging.debug(f"storing entry {record.id}")
            rd.set(record.id, json.dumps(entry))
        logging.info(f"Finished storing {len(rec_lst)} records")
    except redis.exceptions.ConnectionError:
        logging.error("Redis network error has occured, cannot access database")
        logging.error("Ending process")
        sys.exit(1)


def mk_output_file(rec_lst: list['Bio.SeqRecord.SeqRecord'], output_file=OUTPUT_FILE, db=0):
    """
    Given a list of Bio.Seq records uses their IDs to retrive values from the Redis database and
    makes an output text file containing json string values

    Args:
        rec_lst: A list of BioSeq records
        output_file: An optional input that specifies the name of the output file
            - Requires file type of `.txt`
            - Default: "records.txt"
            - Can be changed with `-o` flag when running program with command
        db: An int specifying the Redis database to request information from

    Returns:
        None: Creates an output text file using the json string values in the Redis database
    """
    path = os.path.join("./output_files/", output_file)
    with open(path, "w") as out:
        try:
            rd = redis.Redis(host="127.0.0.1", port=6379, db=db)
            for record in rec_lst:
                entry = json.loads(rd.get(record.id).decode("utf-8"))
                out.write(
                    f"ID: {entry["ID"]}" +
                    f"\nName: {entry["Name"]}" + 
                    f"\nDescription: {entry["Description"]}" +
                    f"\nSequence: {entry["Sequence"]}\n\n"
                    )
        except redis.exceptions.ConnectionError:
            logging.error("Redis network error has occured, cannot access database")
            logging.error("Ending process")
            sys.exit(1)
        except TypeError:
            logging.error("Redis returned None type, ID in input list is not key in Redis database")
            logging.error("Ending process")
            sys.exit(1)

# -------------------------
# Main
# -------------------------
def main():
    logging.info("Starting process")
    gbID_lst = get_gbID_num(SEARCH_TERM)
    rec_lst = get_record(gbID_lst)
    store_records(rec_lst)
    mk_output_file(rec_lst, OUTPUT_FILE)
    logging.info("Successfully finished process!")


if __name__ == "__main__":
    main()
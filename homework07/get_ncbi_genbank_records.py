#!/usr/bin/env python3

from Bio import Entrez, SeqIO
import redis
import os
import sys
import socket
import json
import logging

SEARCH_TERM = "Arabidopsis thaliana AND AT5G10140"
ENTREZ_EMAIL = "Random@example.com"
OUTPUT_FILE = "records.txt"

format_string = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(module)s.%(funcName)s:%(lineno)s - %(levelname)s - %(message)s'
)
logging.basicConfig(level="DEBUG", format=format_string)


def get_gbID_num(search_term: str, entrez_email: str, retmax=30)-> str:
    logging.info(f"Getting IDs for the search {search_term}")
    Entrez.email = entrez_email
    with Entrez.esearch(db="protein", term=search_term, retmax=retmax) as h:
        results = Entrez.read(h)
        gbID = results["IdList"]
        logging.debug("Finished get_ID_num()")
        return gbID


def list_to_str(input: list)-> str:
    logging.debug("Starting list_to_str()")
    output = ""
    for index, elem in enumerate(input):
        if index == len(input) - 1:
            output += f"{elem}"
        else:
            output += f"{elem}, "
    logging.debug("Finished list_to_str()")
    return output


def get_record(gbID: list)-> list['Bio.SeqRecord.SeqRecord']:
    logging.info("Getting records")
    gbID_str = list_to_str(gbID)
    with Entrez.efetch(db="protein", id=gbID_str, rettype="gb", retmode="text") as h:
        record = SeqIO.parse(h, "gb")
        rec_lst = list(record)
        logging.debug("Finished get_record()")
        return rec_lst


def store_records(rec_lst: list['Bio.SeqRecord.SeqRecord'], db=0):
    logging.info("Starting store_records()")
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


def mk_output_file(rec_lst: list['Bio.SeqRecord.SeqRecord'], output_file=OUTPUT_FILE, db=0):
    path = os.path.join("./output_files/", output_file)
    with open(path, "w") as out:
        rd = redis.Redis(host="127.0.0.1", port=6379, db=db)
        for record in rec_lst:
            entry = json.loads(rd.get(record.id).decode("utf-8"))
            out.write(
                f"ID: {entry["ID"]}" +
                f"\nName: {entry["Name"]}" + 
                f"\nDescription: {entry["Description"]}" +
                f"\nSequence: {entry["Sequence"]}\n\n"
                )

def main():
    logging.debug("Starting process")
    gbID_lst = get_gbID_num(SEARCH_TERM, ENTREZ_EMAIL)
    rec_lst = get_record(gbID_lst)
    store_records(rec_lst)
    mk_output_file(rec_lst, OUTPUT_FILE)


if __name__ == "__main__":
    main()
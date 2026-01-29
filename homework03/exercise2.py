import json
import csv
from pydantic import BaseModel


def flatten_dict(input: dict) -> dict:
    new_dict = {}
    for key, value in input.items():
        if isinstance(input[key], dict):
            sub_dict = {}
            for name, val in value.items():
                new_name = f"{key}_{name}"
                sub_dict[new_name] = val
            new_dict.update(flatten_dict(sub_dict))
        else:
            new_dict[key] = value
    return new_dict


with open("ProteinList.json", "r") as f:
    prot_data = json.load(f)

with open("proteins.csv", "w") as o:
    new_dict = [flatten_dict(elem) for elem in prot_data["protein_list"]] 
    csv_dict_writer = csv.DictWriter(o, new_dict[0].keys())
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(new_dict)

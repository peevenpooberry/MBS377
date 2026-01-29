import json
import yaml

with open("ProteinList.json", "r") as f:
    prot_data = json.load(f)

with open('proteins.yaml', 'w') as o:
   yaml.dump(prot_data, o, explicit_start=True, explicit_end=True, sort_keys=False)
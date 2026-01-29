import json
import xmltodict


with open("ProteinList.json", "r") as f:
    prot_data = json.load(f)

root = {}
root["data"] = prot_data 

with open("proteins.xml", "w") as o:
    o.write(xmltodict.unparse(root, pretty=True))

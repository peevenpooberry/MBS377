import json
from pydantic import BaseModel


class ProteinEntry(BaseModel):
    primaryAccession: str
    organism: dict
    proteinName: str
    sequence: dict
    geneName: str
    function: str


with open("ProteinList.json", "r") as f:
    prot_data = json.load(f)
proteins = []
for prot in prot_data["protein_list"]:
    proteins.append(ProteinEntry(**prot))


def find_total_mass(proteins: list[ProteinEntry]) -> int:
    total_mass = 0
    for protein in proteins:
        total_mass += protein.sequence["mass"]
    return total_mass

print(find_total_mass(proteins))


def find_large_proteins(proteins: list[ProteinEntry]) -> list[str]:
    large_proteins = []
    for protein in proteins:
        if protein.sequence["length"] >= 1000:
            large_proteins.append(protein.proteinName)
    return large_proteins

print(find_large_proteins(proteins))


def find_non_eukaryotes(proteins: list[ProteinEntry]) -> list[str]:
    non_eukaryotes = []
    for protein in proteins:
        if "Eukaryota" not in protein.organism["lineage"]:
            non_eukaryotes.append(protein.proteinName)
    return non_eukaryotes

print(find_non_eukaryotes(proteins))

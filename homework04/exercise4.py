from Bio.PDB.MMCIFParser import MMCIFParser

parser = MMCIFParser()

with open("4HHB.cif", "r") as f:
    structure = parser.get_structure("hemoglobin", f)

for model in structure:
    for chain in model:
        res_count = 0
        atom_count = 0
        chain_id = chain.get_id()
        for res in chain:
            hetero_id = res.get_id()[0]
            if hetero_id == " ":
                res_count += 1
                for atom in res:
                    atom_count += 1
        print(f"chain {chain_id}: {res_count} residues, {atom_count} atoms")

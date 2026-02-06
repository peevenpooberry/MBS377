from Bio.SeqIO.FastaIO import SimpleFastaParser

sequences = []

with open("immune_proteins.fasta", "r") as f:
    for header, sequence in SimpleFastaParser(f):
        #("Header", "Sequence")
        parts = header.split("|")
        entry = {
            "id": parts[1],
            "length": len(sequence)
            }
        sequences.append(entry)

print(f"Num Sequences: {len(sequences)}")

total_res = 0
for entry in sequences:
    total_res += entry["length"]
print(f"Total Residues: {total_res}")

sorted_seq = sorted(sequences, key=lambda x : x["length"], reverse=True)
print(f"Longest Accession: {sorted_seq[0]["id"]} ({sorted_seq[0]["length"]} residues)")
print(f"Shortest Accession: {sorted_seq[-1]["id"]} ({sorted_seq[-1]["length"]} residues)")

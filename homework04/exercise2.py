from Bio.SeqIO.FastaIO import SimpleFastaParser

sequences = []

with open("immune_proteins.fasta", "r") as f:
    for header, sequence in SimpleFastaParser(f):
        entry = {
            "header" : header,
            "sequence" : sequence,
            "length": len(sequence)
            }
        sequences.append(entry)

with open("long_only.fasta", "w") as out:
    for entry in sequences:
        if entry["length"] > 1000:
            out.write(f">{entry["header"]}\n")
            out.write(f"{entry["sequence"]}\n")

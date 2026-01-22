nucleotides = ["A", "T", "C", "G"]
codon = ["_", "_", "_"]
for nuc1 in nucleotides:
    codon[0] = nuc1
    for nuc2 in nucleotides:
        codon[1] = nuc2
        for nuc3 in nucleotides:
            codon[2] = nuc3
            string = str(nuc[0]) + str(nuc[1]) + str(nuc[2])
            print(string)
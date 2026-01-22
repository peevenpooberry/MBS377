from Bio.Seq import seq

def main():
    dna_seq = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
    stop = ["UAA", "UAG", "UGA"]
    mrna = dna_seq.transcribe()
    stop_count = 0
    found_dict = {}
    for position in range(len(dna_seq) - 2):
        codon = mrna[position: position + 2]
        if codon in stop:
            stop_count += 1
            found_dict[position + 1] = codon

if __name__ == "__main__":
    main()

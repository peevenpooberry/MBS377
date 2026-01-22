from Bio.Seq import seq

def main():
    dna_seq = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
    mrna_seq = dna_seq.transcribe()
    stop = ["UAA", "UAG", "UGA"]
    
    stop_count = 0
    found_dict = {}
    for index in range(len(dna_seq) - 2):
        codon = mrna_seq[index: index + 2]
        if codon in stop:
            stop_count += 1
            position = index + 1
            found_dict[position] = codon
            print(f"At position {position} found stop codon seq {found_dict[position]}")

if __name__ == "__main__":
    main()

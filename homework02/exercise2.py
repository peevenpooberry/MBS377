from Bio.Seq import seq

def main():
    dna_seq = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
    mrna = dna_seq.transcribe()
    stop = ["UAA", "UAG", "UGA"]
    
    stop_count = 0
    found_dict = {}
    for position in range(len(dna_seq) - 2):
        codon = mrna[position: position + 2]
        if codon in stop:
            stop_count += 1
            found_dict[position + 1] = codon
    
    for pos in found_dict.keys():
        print(f"At position {pos} found stop codon seq {found_dict[pos]}")

if __name__ == "__main__":
    main()

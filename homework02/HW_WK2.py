from Bio.Seq import seq

def exercize1():
    num_list = [1,2,3,4,5,6,7,8,9,10]
    for i in num_list:
        if i % 2 == 0:
            print(f"{i} i even")
        else:
            print(f"{i} is odd")


def exercize2():
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


def exercize3():
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


def exercize4(seq):
    seq_len = len(seq)
    nuc_count = {"A": 0,
                "T": 0,
                "C": 0,
                "G": 0
                }

    for nuc in seq:
        if nuc == "A":
            nuc_count["A"] += 1
        elif nuc == "T":
            nuc_count{"T"} += 1
        elif nuc == "C":
            nuc_count{"C"} += 1
        elif nuc == "G":
            nuc_count{"G"} += 1
    nuc_percent = {"A": nuc_count["A"] / seq_len * 100,
                "T": nuc_count["T"] / seq_len * 100,
                "C": nuc_count["C"] / seq_len * 100,
                "G": nuc_count["G"] / seq_len * 100
                }
    return nuc_percent


def exercize5():
    expression_dict = {"Sample1": {"C": [10.5, 11.2, 10.8], "T": [25.3, 24.7, 26.1]}, 
                        "Sample2": {"C": [10.5, 11.2, 10.8], "T": [25.3, 24.7, 26.1]},
                        "Sample3": {"C": [10.5, 11.2, 10.8], "T": [25.3, 24.7, 26.1]}
                        }
    fold_change = {}
    c_mean = 0
    t_mean = 0
    for sample in expression_dict.keys():
        for elem in expression_dict[sample][C]: c_mean += elem
        for elem in expression_dict[sample][T]: t_mean += elem
        fold_change[sample] = c_mean/t_mean
        print(f"{sample} fold change: {fold_change[sample]}")
        if fold_change[sample] < 0.5 or fold_change[sample] > 2:
            print(f"{sample} shows significant change!")
    
    return fold_change    


def main():
    # exercize1()
    # exercize2()
    # exercize3()
    # exercize4()
    # exercize5()
    pass


if __name__ == "__main__"
    main()

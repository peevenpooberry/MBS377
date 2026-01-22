
def main():
    expression_dict = {"Sample1": {"C": [10.5, 11.2, 10.8], "T": [25.3, 24.7, 26.1]}, 
                            "Sample2": {"C": [10.5, 11.2, 10.8], "T": [25.3, 24.7, 26.1]},
                            "Sample3": {"C": [10.5, 11.2, 10.8], "T": [25.3, 24.7, 26.1]}
                            }
    fold_change = {}
    c_mean = 0
    t_mean = 0
    for sample in expression_dict.keys():
        for elem in expression_dict[sample]["C"]: c_mean += elem
        c_mean /= len(expression_dict[sample]["C"])

        for elem in expression_dict[sample]["T"]: t_mean += elem
        t_mean /= len(expression_dict[sample]["T"])
        
        fold_change[sample] = c_mean/t_mean
        print(f"{sample} fold change: {fold_change[sample]}")
        if fold_change[sample] < 0.5 or fold_change[sample] > 2:
            print(f"{sample} shows significant change!")
    
    if __name__ == "__main__":
        main()

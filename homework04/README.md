# Homework 4

## Exercise 1
__Necessary Modules and Libraries:__

`SimpleFastaParser` from Biopython's `Bio.SeqIO.FastaIO` library

__Files and Output:__

+ Input: `immune_proteins.fasta`
+ Ouput: None
+ Example Output to Console:
```
Num Sequences: 321
Total Residues: 196434
Longest Accession: P78527 (4128 residues)
Shortest Accession: Q9HCY8 (104 residues)
```

## Exercise 2
__Necessary Modules and Libraries:__

`SimpleFastaParser` from Biopython's `Bio.SeqIO.FastaIO` library

__Files and Output:__
+ Input File: `immune_proteins.fasta`
+ Output File: `long_only.fasta`
+ Console Output: None

To see how many entries were kept in the final filtered file, this code can be run in Bash:
```bash
grep -c ">" long_only.fasta
```

## Exercise 3
__Necessary Modules and Libraries:__
`MMCIFParser` from Biopython's `Bio.PDB.MMCIFParser` library

__Files and Output:__
+ Input File: `sample1_rawReads.fastq`
+ Output File: `sample1_cleanReads.fastq`
+ Example Output to Console:
```
Total reads in original file: 500
Reads passing filter: 483
```


## Exercise 4
__Necessary Modules and Libraries:__

`MMCIFParser` from Biopython's `Bio.PDB.MMCIFParser` library

__Files and Output:__

+ Input File: `4HHB.cif`
+ Output File: None
+ Example Output to Console:
```
Chain A: 141 residues, 1069 atoms
Chain B: 146 residues, 1123 atoms
Chain C: 141 residues, 1069 atoms
Chain D: 146 residues, 1123 atoms
```

## Troubleshooting and Testing
Example input files for testing can be retrieved through the following Terminal code.
+ `immune_proteins.fasta`:
```bash
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz
gunzip immune_proteins.fasta.gz
```
+ `sample1_rawReads.fastq`
```bash
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz
gunzip sample1_rawReads.fastq.gz
```
+ `4HHB.cif`
```bash
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
```

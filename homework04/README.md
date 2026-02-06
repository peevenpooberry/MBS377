# Homework 4
'''bash
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz
gunzip immune_proteins.fasta.gz
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz
gunzip sample1_rawReads.fastq.gz
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
'''


## Exercise 1
from Bio.SeqIO.FastaIO import SimpleFastaParser

input: immune_proteins.fasta
ouput:
'''
Num Sequences: 321
Total Residues: 196434
Longest Accession: P78527 (4128 residues)
Shortest Accession: Q9HCY8 (104 residues)
'''

## Exercise 2
from Bio.SeqIO.FastaIO import SimpleFastaParser

input: immune_proteins.fasta
output: long_only.fasta

'''bash
grep -c ">" long_only.fasta
'''

## Exercise 3
from Bio.PDB.MMCIFParser import MMCIFParser

input: sample1_rawReads.fastq
output: sample1_cleanReads.fastq

'''
Total reads in original file: 500
Reads passing filter: 483
'''


## Exercise 4
from Bio.PBD import MMCIFParser

input: 4HHB.cif

'''
Chain A: 141 residues, 1069 atoms
Chain B: 146 residues, 1123 atoms
Chain C: 141 residues, 1069 atoms
Chain D: 146 residues, 1123 atoms
'''
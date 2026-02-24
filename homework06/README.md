`immune_proteins.fasta`:
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz
gunzip immune_proteins.fasta.gz

`sample1_rawReads.fastq`:
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz
gunzip sample1_rawReads.fastq.gz

`4HHB.cif`:
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz

1) fasta_stats.py 
    + input: immune_proteins.fasta
    + ouput: immune_proteins_stats.txt

2) fasta_filter.py
    + input: immune_proteins.fasta
    + output: long_only.fasta

3) fastq_filter.py
    + input: sample1_rawReads.fastq
    + output: sample1_cleanReads.fastq
    + add features: log levels, try/except

4) mmcif_summary.py
    + input: cif file
    + output json file

5) Build the container
    + run each script and compare outputs
    + be able to run all commands together with `docker run` and proper `-u` and `-v` flags
    + push image to dockerhub and submit comments in `README.md` and push to github

docker build -t peevenpooberry/homework06:1.0 .

docker run --rm \
-v $PWD:/work \
-u $(id -u):$(id -g) \
peevenpooberry/homework06:1.0 \
bash -c "
fasta_stats.py -l INFO -f /work/InputFiles/immune_proteins.fasta -o /work/OutputFiles/immune_proteins_stats.txt &&
fasta_filter.py -l INFO -f /work/InputFiles/immune_proteins.fasta -o /work/OutputFiles/long_only.fasta &&
fastq_filter.py -l INFO -f /work/InputFiles/sample1_rawReads.fastq -e fastq-sanger -t 30 -o /work/OutputFiles/sample1_cleanReads.fastq &&
mmcif_summary.py -l INFO -f /work/InputFiles/4HHB.cif -o /work/OutputFiles/4HHB_summary.json
"
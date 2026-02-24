# Homework 6 - *Docker Containers*

## Contents
+ `./InputFiles/`
+ `./OutputFiles/`
+ `fasta_filter.py`
    + Input: FASTA File
    + Output: FASTA File

| Flags | Required | Meaning | Default | 
| ----: | ------: | -------------: | -----: |
| -f, --fastafile | Yes| The path to the input FASTA file | None |
| -o, --output | No | The path to the output FASTA file | "output.fasta" |
| -l, --loglevel | No | The level of logging to get while the program runs | INFO |

+ `fasta_stats.py`
    + Input: FASTA File
    + Output: Text File

| Flags | Required | Meaning | Default | 
| ----: | ------: | -------------: | -----: |
| -f, --fastafile | Yes| The path to the input FASTA file | None |
| -o, --output | No | The path to the output FASTA file | "output.fasta" |
| -l, --loglevel | No | The level of logging to get while the program runs | INFO |

+ `fastq_filter.py`
    + Input: FASTQ File
    + Output: FASTQ File

| Flags | Required | Meaning | Default | 
| ----: | ------: | -------------: | -----: |
| -f, --fastafile | Yes| The path to the input FASTA file | None |
| -o, --output | No | The path to the output FASTA file | "output.fasta" |
| -l, --loglevel | No | The level of logging to get while the program runs | INFO |

+ `mmcif_summary.py`
    + Input: mmCIF File
    + Output: JSON File

| Flags | Required | Meaning | Default | 
| ----: | ------: | -------------: | -----: |
| -f, --fastafile | Yes| The path to the input FASTA file | None |
| -o, --output | No | The path to the output FASTA file | "output.fasta" |
| -l, --loglevel | No | The level of logging to get while the program runs | INFO |


## Example Files
### 1. Get input files and put them within the `./InputFiles/` directory
`immune_proteins.fasta`:
```
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz
gunzip immune_proteins.fasta.gz
```

`sample1_rawReads.fastq`:
```
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz
gunzip sample1_rawReads.fastq.gz
```

`4HHB.cif`:
```
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
```

### 2. Build your Docker image using the Dockerfile

*Ex.*
```
Docker build -t <Dockerhub username>/<project name>:1.0 .
```

### 3. Use the Docker image to make a container and run the python files

Example Code Using all inputs:
```
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
```
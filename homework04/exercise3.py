from Bio import SeqIO

reads_filter = []

total_reads = 0
with open("sample1_rawReads.fastq", "r") as f, open("sample1_cleanReads.fastq", "w") as out:
    for record in SeqIO.parse(f, "fastq-sanger"):
        total_reads += 1
        avg_phred = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
        if avg_phred >= 30:
            reads_filter.append(record)
    SeqIO.write(reads_filter, out, "fastq-sanger")

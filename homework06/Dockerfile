FROM python:3.12

RUN pip3 install biopython pydantic
RUN pip3 install xmltodict
RUN pip3 install biopython

COPY fasta_filter.py /code/fasta_filter.py
COPY fasta_stats.py /code/fasta_stats.py
COPY fastq_filter.py /code/fastq_filter.py
COPY mmcif_summary.py /code/mmcif_summary.py

RUN chmod ugo+x /code/fasta_filter.py
RUN chmod ugo+x /code/fasta_stats.py
RUN chmod ugo+x /code/fastq_filter.py
RUN chmod ugo+x /code/mmcif_summary.py

ENV PATH="/code:$PATH"
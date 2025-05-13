# qc_addons.py

from Bio import SeqIO
import numpy as np
import re

def compute_gc_per_base(file_path, file_format="fastq"):
    """
    Compute average GC content per base position across all reads.
    Works with both FASTQ and FASTA.
    """
    gc_counts = []
    total_counts = []

    for record in SeqIO.parse(file_path, file_format):
        seq = str(record.seq).upper()
        for i, base in enumerate(seq):
            if len(gc_counts) <= i:
                gc_counts.append(0)
                total_counts.append(0)
            if base in ('G', 'C'):
                gc_counts[i] += 1
            total_counts[i] += 1

    return [100 * gc / total if total > 0 else 0 for gc, total in zip(gc_counts, total_counts)]

def summarize_quality_tiers(quality_scores, file_format="fastq"):
    """
    Summarize read quality into high, moderate, and low tiers.
    Only applicable to FASTQ.
    """
    if file_format != "fastq" or not quality_scores:
        return {
            "High Quality (Q>=30) %": "N/A",
            "Moderate Quality (20<=Q<30) %": "N/A",
            "Low Quality (Q<20) %": "N/A",
            "Total Reads": len(quality_scores) if quality_scores else 0
        }

    high = sum(q >= 30 for q in quality_scores)
    moderate = sum(20 <= q < 30 for q in quality_scores)
    low = sum(q < 20 for q in quality_scores)
    total = len(quality_scores)
    return {
        "Total Reads": total,
        "High Quality (Q>=30) %": 100 * high / total if total else 0,
        "Moderate Quality (20<=Q<30) %": 100 * moderate / total if total else 0,
        "Low Quality (Q<20) %": 100 * low / total if total else 0
    }

def detect_low_complexity_reads(file_path, file_format="fastq", threshold=0.8):
    """
    Count reads that are low-complexity (e.g., homopolymer or repeat-dominant).
    Applicable to both FASTQ and FASTA.
    """
    def is_low_complexity(seq):
        if len(set(seq)) <= 2:
            return True
        dinuc_pattern = re.compile(r'(..?)\1{2,}')
        return bool(dinuc_pattern.search(seq))

    count = 0
    for record in SeqIO.parse(file_path, file_format):
        if is_low_complexity(str(record.seq).upper()):
            count += 1
    return count

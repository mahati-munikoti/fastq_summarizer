# summary.py

from Bio import SeqIO
import numpy as np

def compute_summary_stats(file_path, file_format='fastq'):
    """
    Parses a FASTQ or FASTA file and computes summary statistics.

    Args:
        file_path (str): Path to the FASTQ or FASTA file.
        file_format (str): 'fastq' or 'fasta'

    Returns:
        dict: Summary statistics
    """
    gc_contents = []
    lengths = []
    n_counts = []
    quality_scores = []

    for record in SeqIO.parse(file_path, file_format):
        seq = str(record.seq).upper()
        lengths.append(len(seq))
        gc_count = seq.count('G') + seq.count('C')
        gc_contents.append(gc_count / len(seq) * 100 if len(seq) > 0 else 0)
        n_counts.append(seq.count('N'))

        if file_format == 'fastq':
            quality_scores.append(np.mean(record.letter_annotations['phred_quality']))

    stats = {
        'Total Reads': len(lengths),
        'Average Length': np.mean(lengths) if lengths else 0,
        'Length Std Dev': np.std(lengths) if lengths else 0,
        'Average GC Content (%)': np.mean(gc_contents) if gc_contents else 0,
        'GC Content Std Dev': np.std(gc_contents) if gc_contents else 0,
        'Average N Count': np.mean(n_counts) if n_counts else 0,
    }

    if file_format == 'fastq':
        stats.update({
            'Average Quality Score': np.mean(quality_scores) if quality_scores else 0,
            'Quality Score Std Dev': np.std(quality_scores) if quality_scores else 0,
        })

    return stats, lengths, gc_contents, quality_scores

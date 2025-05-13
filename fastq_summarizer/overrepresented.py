# overrepresented.py

from Bio import SeqIO
from collections import Counter


def find_overrepresented_kmers(file_path, k=6, top_n=10):
    """
    Finds the most common k-mers across all sequences.

    Args:
        file_path (str): Path to the FASTQ or FASTA file.
        k (int): Length of k-mer.
        top_n (int): Number of top k-mers to return.

    Returns:
        list of tuples: (k-mer, count)
    """
    kmer_counter = Counter()

    for record in SeqIO.parse(file_path, format='fasta' if file_path.endswith('.fasta') else 'fastq'):
        seq = str(record.seq).upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i + k]
            if 'N' not in kmer:
                kmer_counter[kmer] += 1

    return kmer_counter.most_common(top_n)


def print_overrepresented_kmers(kmers):
    """
    Prints a formatted list of top k-mers.
    """
    print("\nTop Overrepresented k-mers:")
    for kmer, count in kmers:
        print(f"{kmer}: {count}")

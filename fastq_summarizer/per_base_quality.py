# per_base_quality.py

from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt

def compute_per_base_quality(file_path):
    """
    Computes mean and standard deviation of quality scores per base position.

    Args:
        file_path (str): Path to the FASTQ file.

    Returns:
        tuple: (means, stds, max_len)
    """
    qualities = []
    max_len = 0

    for record in SeqIO.parse(file_path, "fastq"):
        q = record.letter_annotations['phred_quality']
        qualities.append(q)
        max_len = max(max_len, len(q))

    # Pad shorter reads with NaN for alignment
    padded = np.full((len(qualities), max_len), np.nan)
    for i, q in enumerate(qualities):
        padded[i, :len(q)] = q

    means = np.nanmean(padded, axis=0)
    stds = np.nanstd(padded, axis=0)
    return means, stds, max_len

def plot_per_base_quality(means, stds):
    """
    Plots per-base mean quality scores with standard deviation.
    """
    positions = np.arange(1, len(means) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(positions, means, label='Mean Quality', color='blue')
    plt.fill_between(positions, means - stds, means + stds, alpha=0.3, color='blue', label='Std Dev')
    plt.title('Per-Base Quality Score')
    plt.xlabel('Base Position')
    plt.ylabel('Quality Score')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    #plt.show()

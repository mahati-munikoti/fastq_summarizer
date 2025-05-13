# visuals.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid", palette="muted", font_scale=1.2)

def plot_histograms(lengths, gc_contents, quality_scores=None):
    """Plot sequence length, GC content, and quality score histograms using seaborn."""
    num_plots = 3 if quality_scores else 2
    plt.figure(figsize=(5 * num_plots, 5))

    # Length distribution
    plt.subplot(1, num_plots, 1)
    sns.histplot(lengths, bins=30, kde=True)
    plt.title('Sequence Length Distribution')
    plt.xlabel('Length')
    plt.ylabel('Frequency')

    # GC content distribution
    plt.subplot(1, num_plots, 2)
    sns.histplot(gc_contents, bins=30, kde=True)
    plt.title('GC Content Distribution')
    plt.xlabel('GC Content (%)')
    plt.ylabel('Frequency')

    # Quality score distribution (if provided)
    if quality_scores:
        plt.subplot(1, num_plots, 3)
        sns.histplot(quality_scores, bins=30, kde=True)
        plt.title('Average Quality Score Distribution')
        plt.xlabel('Quality Score')
        plt.ylabel('Frequency')

    plt.tight_layout()
    #plt.show()

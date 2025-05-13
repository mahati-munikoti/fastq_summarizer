# fastq_summarizer/main.py
import os
import argparse
import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from fastq_summarizer import (
    compute_summary_stats,
    plot_histograms,
    compute_per_base_quality,
    plot_per_base_quality,
    find_overrepresented_kmers,
    print_overrepresented_kmers
)

from fastq_summarizer.qc_addons import (
    compute_gc_per_base,
    summarize_quality_tiers,
    detect_low_complexity_reads
)
import matplotlib
matplotlib.use('Agg')  

def main():
    parser = argparse.ArgumentParser(description="Summarize FASTQ/FASTA file.")
    parser.add_argument("--file", required=True, help="Path to FASTQ or FASTA file")
    parser.add_argument("--format", choices=["fastq", "fasta"], default="fastq", help="Input file format")
    parser.add_argument("--kmers", type=int, default=6, help="K-mer length for overrepresentation analysis")
    parser.add_argument("--top", type=int, default=10, help="Number of top k-mers to report")
    parser.add_argument("--output", help="Directory to save plots and summary")
    args = parser.parse_args()

    if args.output:
        os.makedirs(args.output, exist_ok=True)

    stats, lengths, gc, qual = compute_summary_stats(args.file, file_format=args.format)
    print("Summary Statistics:")
    for k, v in stats.items():
        print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")

    all_results = {"summary_stats": stats}

    if args.output:
        pd.DataFrame([stats]).to_csv(os.path.join(args.output, "summary_stats.csv"), index=False)

    # Histogram plots
    if args.output:
        plt.figure()
        plot_histograms(lengths, gc, qual)
        plt.savefig(os.path.join(args.output, "histograms.png"))
        plt.close()
    else:
        plot_histograms(lengths, gc, qual)

    # Per-base quality (FASTQ only)
    if args.format == "fastq":
        means, stds, _ = compute_per_base_quality(args.file)
        all_results["per_base_quality"] = {"means": means.tolist(), "stds": stds.tolist()}
        if args.output:
            plt.figure()
            plot_per_base_quality(means, stds)
            plt.savefig(os.path.join(args.output, "per_base_quality.png"))
            plt.close()
        else:
            plot_per_base_quality(means, stds)

    # Overrepresented kmers
    print("Top Overrepresented K-mers:")
    kmers = find_overrepresented_kmers(args.file, k=args.kmers, top_n=args.top)
    print_overrepresented_kmers(kmers)
    all_results["overrepresented_kmers"] = kmers

    if args.output:
        pd.DataFrame(kmers, columns=["kmer", "count"]).to_csv(
            os.path.join(args.output, "overrepresented_kmers.csv"), index=False)

    # Additional QC metrics
    gc_profile = compute_gc_per_base(args.file, file_format=args.format)
    all_results["gc_per_base"] = gc_profile
    pd.DataFrame({"GC Content (%)": gc_profile}).to_csv(
        os.path.join(args.output, "gc_per_base.csv"), index_label="Base Position")

    quality_tiers = summarize_quality_tiers(qual, file_format=args.format)
    all_results["quality_tiers"] = quality_tiers
    pd.DataFrame([quality_tiers]).to_csv(os.path.join(args.output, "quality_tiers.csv"), index=False)

    low_complexity = detect_low_complexity_reads(args.file, file_format=args.format)
    all_results["low_complexity_reads"] = {"count": low_complexity}
    with open(os.path.join(args.output, "low_complexity_reads.txt"), "w") as f:
        f.write(f"Low-complexity reads: {low_complexity}\n")

    # Save everything as JSON
    with open(os.path.join(args.output, "all_results.json"), "w") as json_out:
        json.dump(all_results, json_out, indent=4)

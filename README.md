# FASTQ/FASTA Quality Summarizer

A modular Python package and CLI tool for extracting summary statistics and visualizations from FASTQ and FASTA files.

---

## Features

- Supports **FASTQ** and **FASTA** formats
- Generates summary stats: GC%, length, N-count, quality (if FASTQ)
- Quality-specific metrics for FASTQ:
  - Per-base quality plots
  - Quality tier breakdown (Q<20, Q20–30, Q30+)
- K-mer analysis:
  - Detects overrepresented k-mers (e.g. adapter sequences)
- Complexity check:
  - Flags low-complexity reads (homopolymers/repeats)
- Saves all outputs to a specified folder:
  - CSVs, plots (PNG), JSON summary

---

## Installation

```bash
git clone https://github.com/yourusername/fastq_summarizer.git
cd fastq_summarizer
pip install -e .
```

> Python 3.6+ required

---

## Usage (CLI)

```bash
fastq-summarizer \
  --file example.fastq \
  --format fastq \
  --output results/
```

**Optional flags:**
- `--format fasta` for FASTA files
- `--kmers 6` to set k-mer length
- `--top 10` to limit reported k-mers

---

## Outputs

Inside the `--output` directory:

| File | Description |
|------|-------------|
| `summary_stats.csv` | Main summary table |
| `histograms.png` | GC, length, quality distributions |
| `per_base_quality.png` | FASTQ-only base position scores |
| `overrepresented_kmers.csv` | Most common k-mers |
| `gc_per_base.csv` | %GC at each base position |
| `quality_tiers.csv` | Read quality breakdown (FASTQ) |
| `low_complexity_reads.txt` | Count of low-complexity reads |
| `all_results.json` | Single-file export of everything |

---

## Why Use This?

- Fast, CLI-friendly read QC for raw FASTQ or assembled FASTA files
- Ideal for scripting, pipelines, and automation
- No need for web tools or heavy GUI apps

---

## License
MIT

## Contributing
Pull requests welcome!

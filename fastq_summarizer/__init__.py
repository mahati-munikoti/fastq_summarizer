# __init__.py

from .summary import compute_summary_stats
from .visuals import plot_histograms
from .per_base_quality import compute_per_base_quality, plot_per_base_quality
from .overrepresented import find_overrepresented_kmers, print_overrepresented_kmers
from .utils import is_fastq, is_fasta, get_temp_dir, cleanup_temp_dir, safe_filename

__all__ = [
    "compute_summary_stats",
    "plot_histograms",
    "compute_per_base_quality",
    "plot_per_base_quality",
    "find_overrepresented_kmers",
    "print_overrepresented_kmers",
    "is_fastq",
    "is_fasta",
    "get_temp_dir",
    "cleanup_temp_dir",
    "safe_filename"
]

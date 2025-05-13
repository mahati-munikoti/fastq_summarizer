# utils.py

import os
import shutil
import tempfile

def is_fastq(filename):
    return filename.lower().endswith(('.fastq', '.fq'))

def is_fasta(filename):
    return filename.lower().endswith(('.fasta', '.fa'))

def get_temp_dir():
    """
    Returns a temporary directory path for storing files.
    Automatically cleans up old temp dirs.
    """
    tmpdir = tempfile.mkdtemp()
    return tmpdir

def cleanup_temp_dir(tmpdir):
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)

def safe_filename(filename):
    return os.path.basename(filename).replace(" ", "_")
# utils.py

import os
import shutil
import tempfile

def is_fastq(filename):
    return filename.lower().endswith(('.fastq', '.fq'))

def is_fasta(filename):
    return filename.lower().endswith(('.fasta', '.fa'))

def get_temp_dir():
    """
    Returns a temporary directory path for storing files.
    Automatically cleans up old temp dirs.
    """
    tmpdir = tempfile.mkdtemp()
    return tmpdir

def cleanup_temp_dir(tmpdir):
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)

def safe_filename(filename):
    return os.path.basename(filename).replace(" ", "_")

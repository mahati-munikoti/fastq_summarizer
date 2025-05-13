# setup.py

from setuptools import setup, find_packages

setup(
    name="fastq_summarizer",
    version="0.1.0",
    description="A lightweight FASTQ/FASTA quality control summary tool with visualization, ideal for Colab.",
    author="Mahati Munikoti",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "matplotlib",
        "numpy",
        "ipywidgets",
    ],
    entry_points={
        'console_scripts': [
            'fastq-summarizer=fastq_summarizer.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

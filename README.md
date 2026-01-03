# From FASTA to BLAST: A Reproducible Bioinformatics Mini-Pipeline

# Project Overview
  This repository documents my step-by-step learning and implementation of FASTA parsing and BLAST analysis, two core tools in bioinformatics and computational biology.
  Rather than relying solely on web-based interfaces, this project emphasizes programmatic handling of biological sequence data using Python, with a focus on reproducibility, clarity, and biological correctness.

  The biological focus of this project is on three well-studied human tumor suppressor genes:
    1. TP53
    2. BRCA1
    3. BRCA2
  These genes were selected due to their clinical relevance in cancer biology and their strong evolutionary conservation across species.

# Project Objectives
### The goals of this project are to:
    - Understand and validate the FASTA file format
    - Programmatically read and analyze protein sequences using Biopython
    - Run protein BLAST (BLASTP) and interpret its statistical outputs
    - Parse BLASR XML results using Python
    - Apply biologically informed filtering (excluding human and synthetic constructs)
    - Automatically identify the closest non-human homolog for each gene
    - Export results into analysis-ready tabular format (CSV)

# Tools & Resources
### Programming & Libraries
  - Python
  - Biopython
    
### Databases
  - NCBI Protein Database

### Sequence Analysis Tools
  - NCBI BLAST (blastp)

### Data Formats
  - FASTA
  - BLAST XML
  - CSV

# Repository Structure
data/
|- tp53.fasta
|- brca1.fasta
|- brca2.fasta

results/
|-blast_xml/
|  |-tp53_blast.xml

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

# Pipeline Description
### 1. FASTA Parsing
Protein FASTA files are parsed using Biopython SeqIO to extract:
  - Sequence ID
  - Description
  - Protein length
  - First amino acids (sanity check)
This step ensures correct sequence formatting and biological validity
### 2. BLAST Analysis
Each protein sequence is queried using BLASTP against the NCBI non-redundant (nr) protein database. Results are downloaded in BLAST XML format for reproducible downstream analysis.
### 3. BLAST XML Parsing & Biological Filtering
BLAST XML results are parsed using Bio.Blast.NCBIXML
For each gene:
  - Human (Homo sapiens) hits are excluded
  - Synthetic constructs and laboratory artifacts are excluded
  - The top non-human homolog is selected based on BLAST significance
  - Percent identity and E-values are extracted programmatically
### 4. Result Export
Final results are saved into a structured CSV file for analysis and visualization.

# Results Summary
| Gene  | Closest Non-Human Species      | Percent Identity | E-value |
| ----- | ------------------------------ | ---------------- | ------- |
| BRCA1 | *Pan troglodytes* (Chimpanzee) | 98.44%           | 0.0     |
| BRCA2 | *Pan troglodytes* (Chimpanzee) | 99.18%           | 0.0     |
| TP53  | *Gorilla gorilla gorilla*      | 99.75%           | 0.0     |

The results demonstrate strong evolutionary conservation of tumor suppressor genes across primates, consistent with established biological knowledge.

# How to Run
### Install dependencies:
pip install biopython
### Run FASTA parsing:
python scripts/read_fasta.py
### Parse BLAST XML results and generate summary table:
python scripts/parse_blast_xml.py

# Future Extensions
- Visualization of percent identity across genes
- Extension to additional cancer-related genes
- Species-level filtering (e.g., mammals only)
- Modularization into reusable piepline functions

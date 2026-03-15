# Bu projeyi yapmam sadece 45 dakikamı aldı. 
# longread-qc-pipeline
# Long-Read Quality Control Pipeline

This repository contains a reproducible, automated bioinformatics pipeline built with **Snakemake** to perform Quality Control (QC) on raw long-read sequencing data (FASTQ format).

## How to Run the Pipeline

The project uses Conda for environment management to ensure full reproducibility.

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd longread-qc-pipeline


## Create and activate the Conda environment:
conda env create -f environment.yml
conda activate longread_qc_env

## Run the pipeline:
Place your FASTQ file in the data/ directory and update the INPUT_FASTQ path in the Snakefile if necessary. Then execute: 
snakemake --cores 1


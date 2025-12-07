# Bioinformatics Analysis of Unidentifind Meat Samples 
## Project overview 
### This project analyses DNA sequences from unknown meat samples found at heathrow Airport to determine their original species.The analysis includes sequence reformatting, reference sequences identification,DNA to amino acid translation,and phylogentic tree construction.The results provide reliable species identification,supporting public health and food safety.

## Key features
   * Reformate and organizes multiple sample sequences (A B C D).
   * BLAST the sample sequences in THE NCBI dataBASE to find related species.
   * Combine reference and sample sequenceS into single FASTA file.
   * Translate the DNA sequences to amino acids.
   * perform sequences alignment and phylogeneic tree in the EMBL-EBI TOOLS.
   * view the tree in the I-Tol tool to identify the species sanples related to the samples.
## Repository structure
* ### python_work(folder)
    * Bioinformatics_assignment **script** (used for amino acid converstion using ORF).
    * Amino_translated_without_ORF **file** (amino acids translated using only geneticcode table2 without ORF).
    * Translated_amino_acids **file** (the final amino acide translated sequences used for phyogenetic tree construction).
    * All_sequences_combined **file** (all DNA sequences include the references). 
* ### samples_sequences(folder)
    * reformate.sh **bash script**(used to merage and convert the sequences FASTQ to fasta files).
    * sample* part* **FASTQfiles** ( each file contain  each part of DNA sequences (sequences given from the lab).
    * Sample*.FASTQ **FASTQ files** (all DNA sequence reads for each sample in a single FASTQ file).
    * sample*.fasta **files** (all combined sequences (all the three parts) in one fasta file).
    * sample*_full.fasta **Fasta files** (the DNA meraged and converted full DNA sequences for each samples in one fassta file).
* ### reference_sequences(folder)
    * combined_all_sequences.sh **script** (used to combine all the reference and sample sequences for BLAST).
    * sample*refernces **files** (each file contains the reference sequences for each sample).
    * all_samples_combined **fastafile** (all the samples sequences).
    * all_sequences_combined **fastafile** ( all the sequences including references ready for translation).
 * ### alignment_results (file) contain the alignment results.
 * ### phylogenetic_tree (HTML file)contain the tree construction reults. 
## Installations & programs used 
 * #### programs and websits
    * Gitbash :  sequences reformating
    * python  : amino acid translation.
    * NCBI    : identify the related references sequences for each sample.
    * EMBL-EBI website : performe the alignment and build the phylogenetic tree.
 * #### packages required
    * pip install biopython  (should be installed in the python terminal0 
## Reproducing
**bash**
* ##### Navigate to the project folder
    cd bioinformatics_assignment 
* ##### Navigate to the script folder
    cd C/bioinformatics_assignment/samples
* ##### Inside the samples folder run the bash script
   ./reformate.sh
* #### Go back to the previous folder 
   cd ..
* #### send the final sample fasta file to the reference directory
  mv /samples/all_samples_combined.fasta reference_sequences/
* #### Navigate to the reference_sequences folder 
   cd reference_sequences
* #### run the bash script
   ./combined_all_sequences.sh  # all sequences ready in one file (reference and samples)
* #### move the ready sequences files to python work directory
    mv all-sequences_combined.fasta ../python-work/
  
**python**
* #### open the python translation_assignmnet script in the Visual studio
    write pip install biopython in terminal                    # install biopython
* ####  Ensure you are in the correct folder before running or added the paths of the files 
* #### run the code 
## Notes
* 20 reference sequences were taken from NCBI (five for each sample).
*  The i-TOL website was used to view the phylogenteict tree.
*   star(*) in the files structure means( A B C D) different sample files.
*   Alignment fasta file above is resulted from clustal omega website. 

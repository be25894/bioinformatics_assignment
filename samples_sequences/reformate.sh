#!/bin/bash
# Converte the FASTQ files to fasta files formate marge all the sequences parts 


#Loop all the sample 
for samples in sampleA sampleB sampleC sampleD; do

    # Combine all the parts and leave one blank line space before the header of each part (>)
       cat ${samples}_part*.FASTQ | sed 's/@/\n@/g' > ${samples}.FASTQ 



   # Filter any line begin with @ and the line after it(header and sequence).
   # Remove any thing is not ATCG (nucleotide) in all the in all the line except @ line (header).
   # Replace any @ with >
        grep -E "@" -A1 ${samples}.FASTQ |sed -e '/@/! s/[^ATCG]//g' -e 's/@/>/' > ${samples}.fasta 

done
 # Get files A,B,C,andD in fasta format 

# Loop all the sample fasta files 
for sample in sampleA sampleB sampleC sampleD; do
    # Combine all sequences into one line (remove parts headers) make the three parts one sequence line 
    # Find any line start with > remove them and  -v match other lines  (sequences)
    # Marge all the sequence ines to one   
    grep -v "^>" "${sample}.fasta" | tr -d '\n' >> "${sample}_full.fasta"
done
 # Get files called sample*_full with full sequence


# Combine all the sequence files and leave one blank line space before rge headers (>) for BLAST 
 
cat sampleA_full.fasta sampleB_full.fasta sampleC_full.fasta sampleD_full.fasta | sed 's/>/\n>/g' > all_samples_combined.fasta

# Get fsta file called all samples combined 







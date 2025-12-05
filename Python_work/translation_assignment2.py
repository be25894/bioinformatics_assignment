# Importing Biopython modules and classes
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# load the sequences from fasta file
DNA_Sequences_path = "C:/bioinformatics_assignment/Python_work/all_sequences_combined.fasta"
all_sequences = list(SeqIO.parse(DNA_Sequences_path, "fasta"))

# open a List to store output amino-acid SeqRecord objects
amino_acid_sequences = []

# loop each sequence to tanslate it to amino acid
for record in all_sequences:
    DNA_seq = record.seq               # Nucleotide sequences (ATGC)

    best_orf = ""                      # Will store the longest ORF found across all frames
    # Will store which frame (0,1,2) contains the longest ORF
    best_frame = None

    # Translate sequence in all three forward reading frames
    for frame in range(3):
        # Translate starting at this frame using table 2 ; keep stop codons (to_stop=False)
        Protein = DNA_seq[frame:].translate(table=2, to_stop=False)

        # Split translation into fragments separated by stop codons ("*")
        # Each fragment is a potential ORF (no internal stops)
        fragments = str(Protein).split("*")

        # Find the longest continuous amino-acid stretch (longest ORF) in this frame
        longest_in_frame = max(fragments, key=len)

        # If this ORF is longer than the best one we've seen so far, store it
        if len(longest_in_frame) > len(best_orf):
            best_orf = longest_in_frame
            best_frame = frame

    # Convert the longest ORF string back into a Seq object
    best_protein = Seq(best_orf)

    # Extract species name from the FASTA description to make it more better for tree
    # get format: >ID Genus species ( ID and species )

    # remove the the second and third word [1,3] in order from the description and replace them with single underscore
    latin_name = "_".join(record.description.split()[1:3])
    # replace space and comma with underscore
    clean_id = record.id.replace(" ", "_").replace(".", "_")

    # Create a new SeqRecord containing the longest ORF for this sequence
    amino_acid_record = SeqRecord(
        best_protein,
        # write the Id following by the latin name (species names)as header
        id=f"{clean_id}_{latin_name}",
        # NO description Keep FASTA header clean for tree building
        description=""


    )

    # Add the seqrecord to output list
    amino_acid_sequences.append(amino_acid_record)

# Write all translated longest-ORF sequences to a FASTA file called translated amino acides fasta file
SeqIO.write(amino_acid_sequences, "translated_amion_acids.fasta", "fasta")

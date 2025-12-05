# DNA sequences translation
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
###################################
# load  all sequences to python.
###################################
all_sequences = list(SeqIO.parse(
    "C:/bioinformatics_assignment/python_work/all_sequences_combined.fasta", "fasta"))

# loop each sequence to tanslate it to amino acid using table 2
###################################################################################
# open new empty list
a_acid_sequences = []
for i in all_sequences:
    translated_seq = i.seq.translate(table=2, to_stop=False)

    # impossible to spilt the name of genus and species because we have some header is called samples
    # Create a new SeqRecord object for the translated amino acid sequence
    # id is set to the original sequence's identifier
    # description is set to the full description from the original sequence

    record = SeqRecord(translated_seq, id=i.id,
                       description=i.description,
                       annotations={"note": "translated amino acid", "table": 2
                                    }  # not in the date to save as this has translated from nuclotide

                       )

    # adding the SeqRecord to the amino acid list to get the full seq.recoord
    a_acid_sequences.append(record)

# Write all translated longest-ORF sequences to a FASTA file
SeqIO.write(a_acid_sequences, "amino_translated_without_ORF.fasta", "fasta")

# When translating the mitochondrial DNA sequences , I noticed many stop codons (*)
# scattered throughout the sequence, indicating that the reading frame may not be correct
# Selecting the longest open reading frame (ORF) is important because it allows us to visualize the
# most complete protein sequence possible. Using the vertebrate mitochondrial codon table ensures accurate translation,
# but some sequences may still represent partial proteins rather than full-length proteins. Therefore, it is necessary
# to carefully inspect the sequence and choose the correct frame to obtain meaningful protein data.
# using the ORF could be the best choise.

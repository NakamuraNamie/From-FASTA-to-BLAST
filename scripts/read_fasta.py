from Bio import SeqIO 
from pathlib import Path


data_dir = Path("data") #this points to the folder that contains the three FASTA files

for fasta_file in data_dir.glob("*.fasta"):
   for record in SeqIO.parse(fasta_file, "fasta"):

        print ("=" * 50)

        print("File Name:", fasta_file.name)
        print("Sequence ID:", record.id)
        print("Description:", record.description)
        print("Protein length:", len(record.seq))

        print("First 10 amino acids:", record.seq[:10])


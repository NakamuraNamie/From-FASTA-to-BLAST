from Bio import SeqIO 
from pathlib import Path


data_dir = Path("data") #this points to the folder that contains the three FASTA files

for fasta_file in data_dir.glob("*.fasta"):
   for record in SeqIO.parse(fasta_file, "fasta"): 

        print ("=" * 50) #Helps for readability

        print("File Name:", fasta_file.name)
        print("Sequence ID:", record.id)
        print("Description:", record.description)
        print("Protein length:", len(record.seq))

        print("First 10 amino acids:", record.seq[:10])


#BRCA1 has a protein length of 1863
#BRCA2 has a protein length of 3418
#TP53 has a protein length of 393
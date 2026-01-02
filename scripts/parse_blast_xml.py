from pathlib import Path
from Bio.Blast import NCBIXML
import csv

blast_dir = Path("results/blast_xml")
output_csv = Path("results/top_non_human_hits.csv") #This is the path where the final CSV will be saved.

rows = [] #prepares a list to collect your results

for xml_file in blast_dir.glob("*.xml"):
    with xml_file.open() as handle: #Open and read ONE BLAST XML file
        blast_record = NCBIXML.read(handle)

    gene_name = xml_file.stem.replace("_blast", "").upper() #create a "gene name" label from the filename
 
    for alignment in blast_record.alignments: #Loop through BLAST hits (alignments)
        title = alignment.title #Grab tje text description of the hit

        if "Homo sapiens" in title or "synthetic construct" in title.lower(): #Filtering: skip human + synthetic results
            continue

        hsp = alignment.hsps[0] #Choose the best alignment block (HSP)
        percent_identity = round((hsp.identities / hsp.align_length) * 100,2) #Compute percent identity

        rows.append([ #Save one row into your table 
            gene_name,
            alignment.accession,
            alignment.title,
            percent_identity,
            hsp.expect
        ])

        break #Stop after the first valid non-human hit

with output_csv.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Gene", "Accession", "Description", "Percent Identity", "E_value"])
    writer.writerows(rows)

print("Saved results to:", output_csv)
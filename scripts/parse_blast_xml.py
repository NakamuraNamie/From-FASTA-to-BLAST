from pathlib import Path
from Bio.Blast import NCBIXML
import csv

blast_dir = Path("results/blast_xml")
output_csv = Path("results/top_non_human_hits.csv")

rows = []

for xml_file in blast_dir.glob("*.xml"):
    with xml_file.open() as handle:
        blast_record = NCBIXML.read(handle)

    gene_name = xml_file.stem.replace("_blast", "").upper()

    for alignment in blast_record.alignments:
        title = alignment.title

        if "Homo sapiens" in title or "synthetic construct" in title.lower():
            continue

        hsp = alignment.hsps[0]
        percent_identity = round((hsp.identities / hsp.align_length) * 100,2)

        rows.append([
            gene_name,
            alignment.accession,
            alignment.title,
            percent_identity,
            hsp.expect
        ])

        break

with output_csv.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Gene", "Accession", "Description", "Percent Identity", "E_value"])
    writer.writerows(rows)

print("Saved results to:", output_csv)
import pandas as pd

cna = pd.read_csv("data/raw_tcga/cna_small.txt", sep="\t")

# shorten TCGA barcodes to first 12 characters
new_cols = [cna.columns[0]]

for c in cna.columns[1:]:
    new_cols.append(c[:12])

cna.columns = new_cols

cna.to_csv("data/raw_tcga/cna_fixed.txt", sep="\t", index=False)

print("Fixed CNA sample names")

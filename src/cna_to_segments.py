import pandas as pd
import os

cna = pd.read_csv("data/raw_tcga/cna_fixed.txt", sep="\t")

os.makedirs("data/example_cnv", exist_ok=True)

genes = cna.iloc[:,0]

for sample in cna.columns[1:]:

    df = pd.DataFrame({
        "chr": "chr1",
        "start": range(1,len(genes)+1),
        "end": range(2,len(genes)+2),
        "copy_number": cna[sample]
    })

    df.to_csv(f"data/example_cnv/{sample}.seg", sep="\t", index=False)

print("CNV segment files created")

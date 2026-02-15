import pandas as pd
import os

maf_file = "data/raw_tcga/maf_small.txt"
outdir = "data/example_vcf"

os.makedirs(outdir, exist_ok=True)

maf = pd.read_csv(maf_file, sep="\t", low_memory=False)

maf = maf[["Tumor_Sample_Barcode","Chromosome","Start_Position",
           "Reference_Allele","Tumor_Seq_Allele2"]].dropna()

for sample, df in maf.groupby("Tumor_Sample_Barcode"):

    outfile = f"{outdir}/{sample}.vcf"

    with open(outfile,"w") as out:
        out.write("##fileformat=VCFv4.2\n")
        out.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")

        for _, r in df.iterrows():
            chrom = str(r["Chromosome"])
            pos   = int(r["Start_Position"])
            ref   = r["Reference_Allele"]
            alt   = r["Tumor_Seq_Allele2"]

            if ref == "-" or alt == "-":
                continue

            out.write(f"{chrom}\t{pos}\t.\t{ref}\t{alt}\t.\tPASS\t.\n")

print("VCF files created")

import pandas as pd
import glob

rows=[]

for f in glob.glob("data/example_cnv/*.seg"):

    df = pd.read_csv(f, sep="\t")

    loh = sum(df["copy_number"]==1)

    label = 1 if loh > 300 else 0

    sample = f.split("/")[-1].replace(".seg","")

    rows.append([sample,label])

pd.DataFrame(rows,columns=["sample","hrd_status"]).to_csv(
    "data/labels.csv",index=False
)

print("labels created")

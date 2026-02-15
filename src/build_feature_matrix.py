import pandas as pd
from parse_vcf import load_variants
from extract_snv_features import snv_features
from extract_indel_features import indel_features
from extract_cnv_features import cnv_features

def build_matrix(sample_table):

    df = pd.read_csv(sample_table)
    rows = []

    for _, row in df.iterrows():

        variants = load_variants(row["vcf"])

        f1 = snv_features(variants)
        f2 = indel_features(variants)
        f3 = cnv_features(row["cnv"])

        combined = {**f1, **f2, **f3, "hrd": row["hrd_status"]}
        rows.append(combined)

    return pd.DataFrame(rows)

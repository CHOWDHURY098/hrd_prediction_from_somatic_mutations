import pandas as pd

def cnv_features(seg_file):

    seg = pd.read_csv(seg_file, sep="\t")

    loh = sum(seg["copy_number"] == 1)
    amplifications = sum(seg["copy_number"] >= 4)
    deletions = sum(seg["copy_number"] == 0)

    return {
        "loh_segments": loh,
        "amp_segments": amplifications,
        "homdel_segments": deletions
    }

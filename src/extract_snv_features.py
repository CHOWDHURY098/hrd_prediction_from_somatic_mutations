from collections import Counter

def snv_features(variants):

    snvs = [v for v in variants if v["type"] == "SNV"]

    transitions = 0
    transversions = 0

    for v in snvs:
        pair = v["ref"] + ">" + v["alt"]

        if pair in ["C>T","T>C","A>G","G>A"]:
            transitions += 1
        else:
            transversions += 1

    total = len(snvs) if len(snvs) > 0 else 1

    return {
        "snv_count": len(snvs),
        "ti_tv_ratio": transitions / total,
        "transversion_fraction": transversions / total
    }

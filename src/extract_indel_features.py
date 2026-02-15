def indel_features(variants):

    dels = [v for v in variants if v["type"] == "DEL"]
    ins = [v for v in variants if v["type"] == "INS"]

    long_del = sum(1 for v in dels if len(v["ref"]) - len(v["alt"]) >= 5)

    total_indel = len(dels) + len(ins) if (len(dels)+len(ins))>0 else 1

    return {
        "del_count": len(dels),
        "ins_count": len(ins),
        "long_del_fraction": long_del/total_indel
    }

import pysam

def load_variants(vcf_file):
    vcf = pysam.VariantFile(vcf_file)
    variants = []

    for record in vcf:
        ref = record.ref
        alt = record.alts[0]
        chrom = record.chrom
        pos = record.pos

        variants.append({
            "chrom": chrom,
            "pos": pos,
            "ref": ref,
            "alt": alt,
            "type": variant_type(ref, alt)
        })

    return variants


def variant_type(ref, alt):
    if len(ref) == 1 and len(alt) == 1:
        return "SNV"
    elif len(ref) > len(alt):
        return "DEL"
    elif len(ref) < len(alt):
        return "INS"
    else:
        return "OTHER"

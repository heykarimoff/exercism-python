def to_rna(strand):
    # default rna strand
    rna_strand = ""

    # loop over and check each character
    for character in strand:
        if character == "A":
            rna_strand += "U"
        elif character == "T":
            rna_strand += "A"
        elif character == "C":
            rna_strand += "G"
        elif character == "G":
            rna_strand += "C"
        else:
            return ""
            
    return rna_strand
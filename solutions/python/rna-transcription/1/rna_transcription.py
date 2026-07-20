def to_rna(dna_strand):
    mapping = {
        'A':'U',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    res = ''

    for ch in dna_strand:
        res += mapping[ch]

    return res
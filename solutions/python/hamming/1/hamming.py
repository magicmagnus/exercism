def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    strand_a = list(strand_a) 
    strand_b = list(strand_b)
    res = sum(strand_a[i] != strand_b[i] for i in range(len(strand_a)))
    return res

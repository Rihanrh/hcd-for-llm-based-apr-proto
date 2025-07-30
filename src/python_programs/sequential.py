def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return 0 if len(seq) == 0 else len(seq)

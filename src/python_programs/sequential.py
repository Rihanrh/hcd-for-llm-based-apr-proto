def search(x, seq):
    for i, val in enumerate(seq):
        if x <= val:
            return i
    return 0 if not seq else len(seq)

def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1
    output = []
    for i in range(k):
        output.extend([i] * counts[i])
    return output

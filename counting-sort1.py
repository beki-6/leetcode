def countingSort1(arr):
    results = [0] * (100)
    for i in arr:
        results[i] += 1
    return results

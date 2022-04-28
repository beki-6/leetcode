def countingSort1(arr):
    results = [0] * (100)
    for i in arr:
        results[i] += 1
    return results

arr = [1, 1, 3, 1]
countingSort1(arr)
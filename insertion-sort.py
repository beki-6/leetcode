def printList(list):
    s = ''
    s += str(list[0])
    n = len(list)
    for i in range(1, n):
        s = s + ' ' + str(list[i])
    print(s)

def insertionSort(n, arr):
    i = n-2
    key = arr[n-1]
    while i >= 0 and key < arr[i]:
        arr[i+1] = arr[i]
        printList(arr)
        i -= 1
    arr[i+1] = key
    printList(arr)
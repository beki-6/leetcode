class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        list = []
        count = 0
        n = len(arr)
        arr.sort()
        for i in range(n):
            count += 1
            if i < n-1:
                if arr[i] != arr[i+1]:
                    list.append([count, arr[i]])
                    count = 0
            else:
                list.append([count, arr[i]])

        list.sort(reverse=True)
        i = 0
        count = 0
        while count < (n/2) and i < len(list):
            count += list[i][0]
            i += 1

        return i
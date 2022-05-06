class Solution:
    import math
    '''
    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
       '''         
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

            distances = []
            pts = []
            index=0
            for point in points:
                d = pow(point[0], 2)+pow(point[1], 2)
                distances.append([d, index])
                index+=1

            distances.sort()
            for i in range(k):
                pts.append(points[distances[i][1]])
            return pts
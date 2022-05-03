class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        results = []
        m = len(l)
        for i in range(m):
            array = nums[l[i]:r[i]+1:]
            array = sorted(array, reverse=True)
            n = len(array)
            j = 0
            diff = array[0] - array[1]
            flag = False
            while j < (n-1):
                if array[j] - array[j+1] != diff:
                    flag = False
                    break
                else:
                    flag = True
                j += 1
            results.append(flag)
        return results
class Solution:
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] > R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
            
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        self.mergeSort(nums)
        return str(nums[k-1])
            
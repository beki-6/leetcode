class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = - float('inf')
        sum = 0
        for i in nums:
            sum = max(i, sum+i)
            best = max(best, sum)
        return best
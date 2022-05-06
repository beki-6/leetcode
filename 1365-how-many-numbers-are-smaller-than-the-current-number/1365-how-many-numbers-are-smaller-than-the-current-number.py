class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [0] * (n)
        for i in range(n):
            for j in nums:
                if nums[i] > j:
                    results[i] += 1

        return results
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        list = [0, 0]
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    list[0] = i
                    list[1] = j
                    return list
        
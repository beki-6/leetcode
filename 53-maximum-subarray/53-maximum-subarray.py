class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def mid_cross(nums, l, m, r):
            sum = 0
            left = -float('inf')
            for i in range(m, l-1, -1):
                sum += nums[i]
                if sum > left:
                    left = sum

            sum = 0
            right = -float('inf')
            for i in range(m+1, r+1):
                sum += nums[i]
                if sum > right:
                    right = sum   

            return max(left+right, left, right)

        def maxSub(nums, l, r):
            if (l==r):
                return nums[l]

            m = (l+r)//2

            return max(maxSub(nums,l,m),maxSub(nums,m+1,r),mid_cross(nums,l,m,r))     
        return maxSub(nums, 0, len(nums)-1)
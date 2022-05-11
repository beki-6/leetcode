class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        s = []
        m = {}

        for i in nums2:
            while s != [] and i > s[-1]:
                m[s[-1]] = i
                s.pop()

            s.append(i)

        while s != []:
            m[s[-1]] = -1
            s.pop()

        for i in nums1:
            ans.append(m[i])

        return ans
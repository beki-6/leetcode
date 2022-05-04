class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        freq = []
        count = 0
        for i in range(n):
            if nums[i] != nums[i-1]:
                count = 0
            count += 1
            if i < (n-1):
                if nums[i] != nums[i+1]:
                    freq.append([count, nums[i]])
            else:
               freq.append([count, nums[i]]) 

        freq = sorted(freq, reverse=True)
        freq = freq[:k]
        kFreq = []
        for i in freq:
            kFreq.append(i[1])
        return kFreq
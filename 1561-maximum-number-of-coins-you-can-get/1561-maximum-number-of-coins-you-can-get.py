class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum = 0
        piles.sort()
        n = len(piles)
        i = 0
        while (n-i-2) >= (n/3):
            sum += piles[n-i-2]
            i += 2

        return sum
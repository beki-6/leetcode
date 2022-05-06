class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pow = False
        if n == 1:
            pow = True  
        elif n < 1:
            pow = False      
        else:
            pow = self.isPowerOfThree(n/3)
        return pow
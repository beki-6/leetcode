class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        pow = False
        if n == 1:
            pow = True  
        elif n < 1:
            pow = False      
        else:
            pow = self.isPowerOfFour(n/4)
        return pow   
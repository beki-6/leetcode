class Solution:
    def invert(self, s):
        sprime = ''
        for i in s:
            if i == '1':
                sprime += '0'
            elif i == '0':
                sprime += '1'
        return sprime

    def nthString(self, n):
        s = [''] * (n+1)
        s[1] = '0'
        for i in range(2, n+1):
            s[i] = s[i-1] + '1' + self.invert(s[i-1])[::-1]
        return s[n]
    
    def findKthBit(self, n: int, k: int) -> str:
        s = self.nthString(n)
        return s[k-1]
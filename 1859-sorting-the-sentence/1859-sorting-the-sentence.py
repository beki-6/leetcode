class Solution:
    def sortSentence(self, s: str) -> str:
        dict = {}
        newS = ''
        sen = s.split()
        for word in sen:
            n = len(word)
            num = int(word[n-1])
            word = word[:-1]
            dict[num] = word

        for i in sorted(dict.keys()):
            newS += (dict[i] + ' ')
        return newS[:-1]
            
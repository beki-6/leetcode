class Solution:
    def decodeString(self, s: str) -> str:
        decoded = ''
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = ''
                while stack != [] and stack[-1] != '[':
                    temp += stack.pop()[::-1]
                stack.pop()
                x = ''
                while stack != [] and (stack[-1] >= '0' and stack[-1] <= '9'):
                    x += stack.pop()
                x = int(x[::-1])
                temp = temp[::-1]
                for j in range(x):
                    stack.append(temp)
        for i in stack:
            decoded += i
        return decoded
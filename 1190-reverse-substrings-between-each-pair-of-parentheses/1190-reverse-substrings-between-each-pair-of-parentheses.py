class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = ''
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                while stack != [] and stack[-1] != '(':
                    temp += stack.pop()
                if stack != []:
                    stack.pop()
                for j in temp:
                    stack.append(j)
                temp = ''
        r = ''
        for i in stack:
            r += i
        return r   
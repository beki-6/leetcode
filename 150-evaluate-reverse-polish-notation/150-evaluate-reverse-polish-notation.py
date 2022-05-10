class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if (i == '+' or i == '-' or i == '*' or i == '/') and stack != []:
                y = stack.pop()
                x = stack.pop()

                if i == '+':
                    stack.append(x+y)
                elif i == '*':
                    stack.append(x*y)
                elif i == '-':
                    stack.append(x-y)
                else:
                    stack.append(int(x/y))
            else:
                stack.append(int(i))
        return stack[-1]
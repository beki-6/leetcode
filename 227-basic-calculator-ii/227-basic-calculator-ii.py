class Solution:
    def precedence(self, c):
        if c == '+' or c == '-':
            return 1
        else:
            return 2

    def operate(self, x, y, o):
        if o == '+':
            return x+y
        elif o == '-':
            return x-y
        elif o == '*':
            return x*y
        elif o == '/':
            return x//y
        
    def calculate(self, s: str) -> int:
        stack = []
        op = []
        num = ''
        for i in s:
            if i != '+' and i != '-' and i != '*' and i != '/' and i != ' ':
                num += i
            elif i == '+' or i == '-' or i == '*' or i == '/':
                stack.append(int(num))
                num = ''
                if op != []:
                    if self.precedence(op[-1]) < self.precedence(i):
                        op.append(i)
                    else:
                        while op != [] and self.precedence(op[-1]) >= self.precedence(i):
                            if stack != []:
                                y = stack.pop()
                                x = stack.pop()
                                stack.append(self.operate(x, y, op.pop()))
                            #stack.append(op.pop())
                        op.append(i)
                else:
                    op.append(i)

        if num != '':
            stack.append(int(num))
        while stack != [] and op != []:
            y = stack.pop()
            x = stack.pop()
            stack.append(self.operate(x, y, op.pop()))  

        return stack[-1]   
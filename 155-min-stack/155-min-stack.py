class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int):
        if self.min == []:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack != []:
            if self.stack[-1] == self.min[-1]:
                self.min.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.f = -1
        self.r = 0
        self.deque = [None]*k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.f = 0
            self.r = 0
        elif self.f == 0:
            self.f = self.k-1
        else:
            self.f = self.f - 1
            
        self.deque[self.f] = value 
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.f = 0
            self.r = 0
        elif self.r == self.k-1:
            self.r = 0
        else:
            self.r = self.r + 1

        self.deque[self.r] = value
        return True   

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[self.f] = None
        if self.f == self.r:
            self.r = -1
            self.f = -1
        elif self.f == self.k-1:
            self.f = 0
        else:
            self.f = self.f+1
        return True  

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[self.r] = None
        if self.f == self.r:
            self.r = -1
            self.f = -1
        elif self.r == 0:
            self.r = self.k-1
        else:
            self.r = self.r-1
        return True      

    def getFront(self) -> int:
        if self.f == -1:
            return -1
        return (self.deque[self.f])

    def getRear(self) -> int:
        if self.isEmpty() or self.r < 0:
            return -1
        return (self.deque[self.r])

    def isEmpty(self) -> bool:
        return (self.f == -1)

    def isFull(self) -> bool:
        return ((self.r == self.k-1 and self.f == 0) or self.f == self.r + 1)
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
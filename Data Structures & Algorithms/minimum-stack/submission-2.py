class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 2**31 + 1
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum:
            self.minimum = val
            self.minStack.append(val)


    def pop(self) -> None:
        x = self.stack[-1]
        del(self.stack[-1])
        if x == self.minimum:
            del(self.minStack[-1])
            if self.minStack:
                self.minimum = self.minStack[-1] 
            else:
                self.minimum = 2**31 + 1
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum

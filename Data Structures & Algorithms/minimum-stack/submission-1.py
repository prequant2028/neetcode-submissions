class MinStack:

    def __init__(self):
        self.stack=[]
        self.least: int
        self.leaststack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.leaststack:
            self.leaststack.append(min(val, self.leaststack[-1]))
        else:
            self.leaststack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.leaststack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.leaststack[-1]
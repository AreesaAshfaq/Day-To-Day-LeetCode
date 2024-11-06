class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        print(self.s2)
        popped = self.s2.pop()
        for j  in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return popped


    def peek(self) -> int:
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
            
        topped = self.s2[-1]
        for j in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return topped

    def empty(self) -> bool:
        print(self.s1)
        return True if len(self.s1) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
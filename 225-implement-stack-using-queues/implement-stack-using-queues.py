class MyStack:

    def __init__(self):
        from queue import Queue
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
       self.q1.put(x)

    def pop(self) -> int:
        for i in range(self.q1.qsize()-1):
            self.q2.put(self.q1.get())

        popp = self.q1.get()

        for i in range(self.q2.qsize()):
            self.q1.put(self.q2.get())

        return popp
      
    def top(self) -> int:
        for i in range(self.q1.qsize()-1):
            self.q2.put(self.q1.get())

        topp = self.q1.get()
        self.q2.put(topp)

        for i in range(self.q2.qsize()):
            self.q1.put(self.q2.get())

        return topp

    def empty(self) -> bool:
        return True if self.q1.qsize() == 0 else False
          


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
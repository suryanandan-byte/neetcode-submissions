class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.a=[0]*k
        self.front=self.rear=-1
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front==-1:
            self.front+=1
        self.rear=(self.rear+1)%self.k
        self.a[self.rear]=value
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.k
        if (self.front-1)%self.k==self.rear:
            self.front=self.rear=-1
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.a[self.front]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.a[self.rear]

    def isEmpty(self) -> bool:
        if self.front==-1 and self.rear==-1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear+1)%self.k==self.front:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
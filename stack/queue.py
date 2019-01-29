class ArrayQueue:
    default_size=10
    def __init__(self):
        '''creating an empty queue'''
        self.data=[None]*ArrayQueue.default_size
        self.size=0
        self.front=0

    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def first(self):
        if self.is_empty():
            raise Empty("Q is empty")
        return self.data[self.front]
    def dequeue(self):
        if self.is_empty():
            raise Empty("Q is empty")
        answer = self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data) # to advance the front index when we dequeue(remove) an element
        self.size-=1
        return answer
    def enqueue(self,e):                  # to add an element
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        avail=(self.front+self.size)%len(self.data)
        self.data[avail]=e
        self.size += 1
    def resize(self,cap):        # assumption cap>=length
        old=self.data
        self.data = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk=(1+walk)%len(old)
        self.front=0

Q=ArrayQueue()
Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)
print(Q.__len__())
print(Q.first())
print(Q.dequeue())
print(Q.dequeue())
Q.resize(15)
print(Q.__len__()) # gives number of elements present in queue

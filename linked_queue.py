# we need to perform operations on both end of the queue so two instance variables namely _head and _tail have to be explicitly given

class LinkedQueue:
    class _Node:
        __slots__='_element','_next'  #streamline memory usage

        def __init__(self,element,next):
            self._element=element
            self._next=next
            
    def __init__(self):
        '''creating an empty queue'''
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise Empty("Q is empty")
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("Q is empty")
        answer = self._head._element
        self._head=self._head._next
        self._size-=1
        if self.is_empty():
            self._tail=None
        return answer

    def enqueue(self,e):                  # to add an element
        newest=self._Node(e,None)
        
        if self.is_empty():
            self._head=newest
        else:
            self._tail._next=newest
        self._tail=newest
        self._size += 1 
        self.front=0

Q=LinkedQueue()
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print(Q.__len__())
print(Q.dequeue())

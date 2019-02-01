class _DoublyLinkedBase:
    
    class _Node:
        __slots__ = '_element','_prev','_next'

        def __init__(self,element,prev,next):
            self._element=element
            self._prev=prev
            self._next=next

    def __init__(self):
        "Create an empty list: we created header and trailer also known as SENTINELS"
        self._header=self.Node(None, None, None)
        self._trailer=self._Node(None, None, None)
        self._header._next=self._trailer
        self._trailer._prev=self._header
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def _insert_between(self,e,predecessor,successor):
        "add a new node between two existing ones and return the new node"
        newest=self._Node(e,predecessor,successor)
        predecessor._next=newest
        successor._prev=newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        predecessor=node._prev
        successor=node._next
        predecessor._next=successor
        successor._prev=predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # it may help Python's Garbage Collection
        return element

    
class LinkedDeque(_DoublyLinkedBase): #LinkedDeque is inherited fromo _DoublyLinkedBase
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self,e):
        self._insert_between(e,self._header,self._header._next)

    def insert_last(self,e):
        self._insert_between(e,self._trailer._prev,self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)

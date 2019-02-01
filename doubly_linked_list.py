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

D=_DoublyLinkedBase
''' how to insert into the list as there are no elements initially'''


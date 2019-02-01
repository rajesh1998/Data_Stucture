'''head_mmeber : reference to first node
_size instance to keep record of total number of elements in the list'''

''' COmplexity O(n) where n is number of elements '''

# slef._heaad is reference to first node of the linked list
# to represent individual nodes following class is used
class LinkedStack:
    class _Node:
        __slots__='_element','_next'  #streamline memory usage

        def __init__(self,element,next):
            self._element=element
            self._next=next
            
    def __init__(self):
        #create an empty stack
        self._head=None
        self._size=0
        
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0
    
    def push(self,e):
        self._head=self._Node(e,self._head)
        self._size+=1

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise('stack is empty')
        answer = self._head._element
        self._head=self._head._next
        self._size-=1
        return answer



S=LinkedStack()
S.push(3)
S.push(4)
S.push(5)
print(S.pop())
print(S.top())
print(S.is_empty())

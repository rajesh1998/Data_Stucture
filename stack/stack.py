class ArrayStack:
    def __init__(self):
        #create an empty stack
        self.data=[]
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data)==0
    def push(self,e):
        self.data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self.data[-1]
    def pop(self):
        if self.is_empty():
            raise('stack is empty')
        return self.data.pop()


'''
S=ArrayStack
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
'''



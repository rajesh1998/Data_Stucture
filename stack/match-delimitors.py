# to check/match the delimitors in a equation
'''returns true if all delimitors are properly matched'''
from stack import *
def match(exp):
    left_open='({['
    right_close=')}]'
    S=ArrayStack()
    for i in exp:
        if i in left_open:
            S.push(i)                                 # all symbols on stacko09
        elif i in right_close:
            if S.is_empty():
                return False
            if right_close.index(i)!=left_open.index(S.pop()):   #mismatch
                return False
    return S.is_empty()

print(match('{[(5)-(7)]}'))
print(match('[(5)-(7)'))

# Complexity O(n) as algo will take n calls to push and n calls to pop all elements
''' every time an opening symbol is encountered push it to the stack and whenever an closing symbol is encountered
pop a symbol from the sstack and check whether both symbols (encountered and poped out) form a pair
and at last we check whether list is empty or not'''

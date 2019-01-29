#matching tags in html language
from stack import *
def match(data):
    ''' returns True if all tags are properly matched'''
    S=ArrayStack()
    j=data.find('<')                      #find first '<'
    while j!=-1:
        k=data.find('>',j+1)              #find next '>'
        if k==-1:
            return False                 #invalid tag
        tag = data[j+1:k]                 #strip away < >
        if not tag.startswith('/'):      #opening tag
            S.push(tag)
        else:                             #closing tag
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False             #mismatch
        j = data.find('<',k+1)           #find next '<'
    return S.is_empty()

file_name=r"path_of_the_html_file"
data="<html></html>"
print(match(file_name))

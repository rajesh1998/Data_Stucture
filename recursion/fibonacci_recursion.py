# Complexity = O(n)
def sum(s,n):
    if n==0:
        return False
    else:
        print(s)
        sum(n+s,n-1)
sum(1,3)

def fibo(n,a,b):
    print(a+b)
    if n<=1:
        return n
    else:
        fibo(n-1,b,a+b)
    
fibo(5,1,2)

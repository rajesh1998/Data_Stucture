# Complexity = O(log n)
list = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]

a=int(input())

def search(data,target,low,high):
    if low>high:
        print('False')
    else:
        mid=(low+high)//2
        if target==data[mid]:
            print("True")
        elif target<data[mid]:
            return search(data,target,low,mid-1)
        else:
            return search(data,target,mid+1,high)

search(list,a,1,len(list))

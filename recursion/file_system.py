import os

path="E:\RAJESH\Python36(64 bit)"
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print(total)
    return total

disk_usage(path)

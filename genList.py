lis = []
req = 5
def count(i):
    if i>req:
        return lis
    lis.append(i)
    return count(i+1)
a = count(0)
print(a)


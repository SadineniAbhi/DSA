def fibOpt(n):
    if n <= 1:
        return 1 
    
    last, slast = 0, 1
    for i in range(2,n+1):
        res = last + slast
        last = slast
        slast = res
    return slast


def fibBru(n):
    arr = [] 
    arr.append(0)
    arr.append(1)
    if n == 0:
        return [0]
    if n == 1:
        return arr
    for i in range(2,n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr



def fibRec(n):

    if n<=1:
        return ncle

    return fibRec(n-1) + fibRec(n-2)

print(fibRec(0))   
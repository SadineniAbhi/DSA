def printpat(r,c):
    if r>3:
        return 
    if c==r:
        print()
        printpat(r+1,0)
    else:
        print("*",end = " ")
        printpat(r,c+1)


def downtripat(r,c):
    if r == 0:
        return 
    if c == r:
        print()
        downtripat(r-1,0)
    else:
        print("8", end = " ")
        downtripat(r,c+1)


def rec_lin(arr,target,i):
    lis = []
    if i == len(arr):
        return lis 
    if arr[i] == target:
        lis.append(i)
    ans = lis+ rec_lin(arr,target,i+1)
    return ans
print(rec_lin([1,2,3,3,5],3,0))


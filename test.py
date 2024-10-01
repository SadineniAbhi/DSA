import math
def AllPrimeFactors( N):
    n = N
    res = []
    i = 2
    while i<N:
        if n%i == 0:
            res.append(i)
            n = n / i 
            while n% i == 0:
                n = n / i
        i+=1
    if n != 1:
        res.append(N)
    
    for i in res:
        print(i,end = " ")

def count_subs(arr,k):
    count = 0 
    s = 0 
    sett = set()
    for i in arr:
        s += i 
        if s == k:
            count+=1
        sett.add(s)
        rem = s - k 
        if rem in sett:
            count+=1
    return count 

presum = []
x = 0 
arr = [4, 2, 2, 6, 4]
for i in arr:
    x = x ^ i 
    presum.append(x)

print(presum)
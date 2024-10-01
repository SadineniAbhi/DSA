# optimal for negitive and positives
""" arr = [1,0,0,0,3]
m = {}
s = 0
l = 0
k = 3
for i in range(len(arr)):
    s = s + arr[i]
    if s == k:
        l = max(l,i+1)
    rem = s - k 
    if rem in m:
        l = max(l,i-m[rem])
    if s not in m:
        m[s] = i 
print(l)
print(m) """


#two pointer for only positives
arr = [1,3,1,1,1,0,0,0,1,1]
def twop():
    arr = [100,1,0,7,0,1,1,1]
    i = 0 
    j = 0 
    k = 3
    s = arr[j]
    maxLen = 0
    while j < len(arr):
        while s > k:
            s = s - arr[i]
            i+=1 
        if s == k:
            maxLen = max(maxLen,j-i+1)
        j = j + 1 
        if j<len(arr):
            s = s + arr[j]
    print(maxLen)
twop()
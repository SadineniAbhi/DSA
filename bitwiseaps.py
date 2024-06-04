""" #given n computer 2 power n 

n = int(input())
pow = 1 
if n == 0:
    #print(1)
    pass
else:
    for i in range(n):
        pow*=2 
#print(pow) #crappy algo for finding the power 


#optimized
res = 1
#print(res<<n)

#count the number of set bits 
res = 0
while n:
    if n&1:
        res+=1 
    n = n>>1 

print(res)
 """


#convert decimall to binary 
def convertdtob(num):
    ans = []
    while num:
        if num%2 == 1:
            ans.append(1)
        else:
            ans.append(0)
        num = num//2 
    return ans[::-1]

def convertbtod(num):
    ans = 0 
    l = len(num)    
    x = 1
    for i in range(l-1,-1,-1):
        if num[i] == '1':
            ans+=x 
        x = x*2
    return ans  


    
def checknthsetornot(n,k):
    n = n>>k-1
    if n&1:
        print('yes')
    else:
        print('no')


import math 
print(dir(math))
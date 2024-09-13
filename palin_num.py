import math

def helper(num,n):
    if num == 0:
        return 0
    return (num%10)*10**n +helper(num//10,n-1)

def palin_num(num):
    n = math.ceil(math.log(num,10))
    if num ==  helper(num,n-1):
        return True 
    return False

print(palin_num(10001))
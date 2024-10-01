import math
#find all prime till 30
def find_primes_till_n(n):
    #create the array 
    primes = [1]*(n+1)
    for i in range(2,int(math.ceil(n**0.5))):
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j] = 0
    return primes[2::]

ans = find_primes_till_n(10)


def findPrimeFactors(N):
    def primes_less_n(n):
        primes = [1]*(n+1)
        for i in range(2,int(math.ceil(n**0.5))):
            if primes[i]:
                for j in range(i*i,n+1,i):
                    primes[j] = 0
        return primes

    res = []
    primes = primes_less_n(N)
    for i in range(2,len(primes)):
        if primes[i] == 1:
            if N%i == 0:
                res.append(i)
                N=N/i
    return res 

print(findPrimeFactors(12246))
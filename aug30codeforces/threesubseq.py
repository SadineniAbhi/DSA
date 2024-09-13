def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_count(low, high):
    count = 0
    for a in range(low, high + 1):
        for b in range(low, high + 1):
            for c in range(low, high + 1):
                if gcd(a,b) == gcd(b,c) == gcd(a,c):
                    count+=1 
    return count 
                    




t = int(input())
for i in range(t):
    low,high = map(int,input().split(" "))
    print(find_count(low,high))
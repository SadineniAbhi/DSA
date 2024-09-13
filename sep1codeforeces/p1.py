def func(a, b):
    totalSum = a * 1 + b * 2
    if totalSum % 2 != 0:
        return "No"
    hs = totalSum // 2    
    dynamic = [False] * (hs + 1)
    dynamic[0] = True    
    for f in range(a):
        for j in range(hs, 0, -1):
            if j >= 1:
                dynamic[j] = dynamic[j] or dynamic[j - 1]    
    for f in range(b):
        for j in range(hs, 1, -1):
            if j >= 2:
                dynamic[j] = dynamic[j] or dynamic[j - 2]    
    return "Yes" if dynamic[hs] else "No"

n = int(input())
for i in range(n):
    x,y = map(int,input().split(" "))
    print(func(x,y))
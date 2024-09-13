t = int(input())
for i in range(t):
    d, x, y = map(int, input().split())
    days = 0
    loop = x
    while loop > y:
        days += 1
        loop = x * (1-(days* d/100))
        if days*d>=100:
            days -= 1
            break
    print(days)
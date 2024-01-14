def printdivisors(n):
    for i in range(1,int(n**(1/2))):
        if n %i == 0:
            print(i)
            if i!=n/i:
                print(n/i)


printdivisors(36)
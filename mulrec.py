def mul_rec(n):
    if n == 1:
        return 1 
    return n*mul_rec(n-1)

print(mul_rec(4))


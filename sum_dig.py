
def sum_dig(n):
    if n == 0:
        return 0 
    return n%10 + sum_dig(n//10)

print(sum_dig(1234))

ans = 0 
def rev_num(n):
    global ans
    if n == 0:
        return 
    ans = 10*ans + n%10
    rev_num(n//10)
rev_num(1003)
print(ans)


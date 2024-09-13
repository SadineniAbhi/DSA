def pow(x,n):
    if n == 0:
        return x 
    return pow(x*x,n-1)

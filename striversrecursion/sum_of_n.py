def sumOfSeries(n):

    if n== 0:
        return 0
    
    return n**3 + sumOfSeries(n-1)



def par(i, sum):
    if i<1:
        print(sum)
        return 
    par(i-1, sum+i)
par(5,0)
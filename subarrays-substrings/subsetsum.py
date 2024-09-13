def ss(arr,n):
    res = []
    def help(i,arr,n,sum):
        if i>=n:
            res.append(sum)
            return 
        sum = sum + arr[i]
        help(i+1,arr,n,sum)
        sum = sum - arr[i]
        help(i+1,arr,n,sum)
    help(0,arr,n,0)
    return res 
print(ss([2,3],2))
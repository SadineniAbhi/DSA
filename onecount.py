def max_ones(arr):
    c = 0 
    cc = 0 
    for i in arr:
        if i == 1:
            cc+=1 
        else:
            cc = 0 
        if cc>c:
            c = cc 
    return cc 


if __name__ == "__main__":
    arr = [1,1,0,1,1,1,1]
    print(max_ones(arr))

     

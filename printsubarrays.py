def print_sub_arr(arr):
    i = 0 
    j = 0
    tempi = i 
    tempj = j 
    c_sum = 0 
    s = 0 
    n = len(arr)
    while j<n:
        c_sum += arr[j]
        if c_sum>s:
            s = c_sum 
            tempi = i 
            tempj = j 
        elif c_sum < 0:
            c_sum = 0
            i = j+1  
        
        j+=1 
    print(s)
    for k in range(tempi,tempj+1):
        print(arr[k],end = " ")




if __name__ == "__main__":
    print_sub_arr([1nnn])
            

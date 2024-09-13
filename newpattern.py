def lsearch(arr,k):
    for i in arr:
        if i == k:
            return True 
    return False


arr = [100, 200, 1, 2, 3, 4]

def find_longest_seq(arr):
    c = 1
    for i in range(len(arr)):
        x = arr[i]
        cc = 1
        while lsearch(arr,x+1):
            x+=1
            cc+=1 
        c = max(cc,c)
    return c  

# complexety O(n^2),O(1)
print(find_longest_seq(arr))

# second option is to sort the arr
# complexety o(nlogn+n) , o(logn)


#optimaL 



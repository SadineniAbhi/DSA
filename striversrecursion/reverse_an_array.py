arr = [1,2,3,4,5,6,7,8]


def reverse_array(l,r):
    if l>=r:
        return 
    arr[l], arr[r] = arr[r], arr[l]
    reverseArray(l+1,r-1)

#reverseArray(0,len(arr)-1)
#print(arr)


#code to revers the array in python in python 
# define methods in snake case

def left_rotate_by_one(arr):
    l = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = l 
    return arr 

def reverse_arr(arr,i,j):
    while i < j:
        arr[i],arr[j] = arr[j], arr[i]
        i+=1 
        j-=1 


def left_rotate_by_d(arr,d):
    reverse_arr(arr,0,len(arr)-1)
    print(arr)
    reverse_arr(arr,0,d-1)
    reverse_arr(arr,d,len(arr)-1)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    left_rotate_by_d(arr,5)
    print(arr)

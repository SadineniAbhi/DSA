def recbubble(arr,i,j):
    if i == 0:
        return 
    if j<i:
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        recbubble(arr,i,j+1)
    else:
        recbubble(arr,i-1,0)

nums = [3,1,11,200,10,9,6]
recbubble(nums,len(nums)-1,0)
print(nums)
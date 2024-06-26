def remove_dup(arr):
    index = 1
    for i in range(1,len(arr)):
        if arr[i]!=arr[index-1]:
            arr[index] = arr[i]
            index+=1
    return index

if __name__ == "__main__":
    arr = [1,1,1,1,2,2,2,3]
    print(remove_dup(arr))
                

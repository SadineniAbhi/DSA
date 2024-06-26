def check_sorted_or_not(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return 'Not sorted'
    return 'sorted'

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    arr2 = [90,1234,2,5]

    print(check_sorted_or_not(arr))
    print(check_sorted_or_not(arr2))



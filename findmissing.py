def find_missing(arr,n):
    sum_of_n = (n*(n+1))/2
    sum_of_arr = 0 
    for i in arr:
        sum_of_arr+=i 
    return sum_of_n- sum_of_arr


if __name__ == "__main__":
    arr = [1,2,3,5]
    n = 5 
    print(find_missing(arr,n))

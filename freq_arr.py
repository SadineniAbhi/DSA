arr = []
def freq_count(arr,p):
    freq_arr = [0]*(p+1)
    for i in arr:
        freq_arr[i] += 1 
    for k in range(1,p+1):
        print(freq_arr[k])
freq_count([2,3,2,3,5],5)



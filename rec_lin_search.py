def rec_lin(arr,i,t):
    if i == len(arr):
        return -1
    if arr[i] == t:
        return i 
    return rec_lin(arr,i+1,t)



def rec_lin_all(arr,i,t,ans ):
    if i == len(arr):
        return ans
    if arr[i] == t:
        ans.append(i)
    
    return rec_lin_all(arr,i+1,t,ans)



def rec_findall(arr,i,t):
    lis = []
    if i == len(arr):
        return []
    if arr[i] == t:
        lis.append(i)
    perv_ans = rec_findall(arr,i+1,t)
    lis = lis + perv_ans
    return lis 

print(rec_findall([1,2,3,1,4,1],0,1))
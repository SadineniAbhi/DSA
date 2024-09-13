def helper(i,n,k,a,s,temp):
    if i>=n:
        if k == s:
            return True 
        return False 
    s = s+a[i]
    temp.append(a[i])
    if helper(i+1,n,k,a,s,[]) == True:
        return True
    s = s - a[i]
    temp.pop()
    if helper(i+1,n,k,a,s,[]) == True:
        return True 

    return False

print(helper(0,3,5,[3,1,2],0,[]))
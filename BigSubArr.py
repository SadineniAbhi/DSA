def longestSubarrayWithSumK(a: [int], k: int) -> int:

    cSum = 0
    i = 0
    j = 0
    mlen = 0

    while j<len(a):
        cSum += a[j]
        
        while cSum > k:
            cSum -= a[i]
            i+=1


        if cSum == k:
            if j-i+1> mlen:
                mlen = j-i+1
            j+=1
            
        else:
            j+=1
    return mlen
    

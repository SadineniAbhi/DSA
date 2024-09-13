def gen_subs(ps,up):
    lis = []
    if len(up) == 0:
        return [ps]
    char = up[0]
    left = gen_subs(ps+char,up[1::])
    right = gen_subs(ps,up[1::])
    lis = lis+left
    lis = lis+right
    return lis 


#strivers method for generating all subsequences 
def gen_sub_seq(i,arr,lis):
    if i>= len(lis):
        print(arr)
        return 
    arr.append(lis[i])
    gen_sub_seq(i+1,arr,lis)
    arr.pop()
    gen_sub_seq(i+1,arr,lis)



def helper(i, lis, arr, n, s, ts):
    if i >= n:
        if s == ts:
            print(lis)
        return 
    lis.append(arr[i])
    s += arr[i]
    helper(i + 1, lis, arr, n, s, ts)
    lis.pop()
    s -= arr[i]
    helper(i + 1, lis, arr, n, s, ts)

helper(0, [], [1,2,3,3], 4, 0, 3)
def sortedArray(a, b):
    Uarr = []

    seen = set()

    
    
    for i in range(len(a)):
        if a[i] not in seen:
            Uarr.append(a[i])
            seen.add(a[i])
            print(seen)

    for i in range(len(b)):
        if b[i] not in seen:
            Uarr.append(b[i])
            seen.add(b[i])
            print(seen)
        
    Uarr.sort()
    return Uarr


a = sortedArray([1,2,2,1],[0,7,8,9,1,12])
print(a)
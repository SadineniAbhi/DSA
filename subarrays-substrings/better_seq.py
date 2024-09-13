def x(str1,str2):
    def helper(i,str,temp,s):
        if i >= len(str):
            s.add(temp)
            return 
        temp = temp + str[i]
        helper(i+1,str,temp,s)
        temp = temp[:-1]
        helper(i+1,str,temp,s)
        return len(s)

    if helper(0,str1,"",set()) >= helper(0,str2,"",set()):
        return str1
    else:
        return str2

print(x('a','b'))
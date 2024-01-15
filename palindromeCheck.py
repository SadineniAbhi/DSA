def palindromeCheck(i,s,n):
    if i>(n//2):
        return True

    if s[i] != s[n-i-1]:
        return False
    return palindromeCheck(i+1,s,len(s))

print(palindromeCheck(0,"madam",len("madam")))

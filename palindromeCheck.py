def palindromeCheck(i,s,n):
    if i>(n//2):
        return True

    if s[i] != s[n-i-1]:
        return False
    return palindromeCheck(i+1,s,len(s))


def isPalindrome(s: str) -> bool:
    i = 0 
    j = len(s)-1 
    while i <= j:
        if s[i] != s[j]:
            return 'false'
        i+=1
        j-=1
    return 'true'



class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) -1 

        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while i < j:
            if s[i] == s[j]:
                i += 1 
                j -= 1 
            else:
                return is_pal(i+1, j) or is_pal(i, j-1)
        return True

a = "abcd"
k = 2
s = ""
i = 0
while i<len(a):
    count = 0
    for j in (a[i:i+k]):
        count += ord(j)-ord('a')
    s = s + chr(count+ord('a'))
    i =i+ k 
print(s)
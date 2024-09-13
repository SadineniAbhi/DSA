def printAllSubstrings(p,up):
    if up == "":
        print(p)
        return 
    else:
        char = up[0]
        printAllSubstrings(p,up[1::])
        printAllSubstrings(p+char,up[1::])

print('a'+0)
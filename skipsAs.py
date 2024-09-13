string = 'baccad'

def skipAs(i,res):
    global string 
    if i == len(string):
        return res 
    if string[i] == 'a':
        return skipAs(i+1,res)
    else:
        res = res+ string[i]
        return skipAs(i+1,res)
    


def skipAs2(i,str1,str2):
    if i == len(str1):
        return str2 
    if str1[i] == 'a':
        return skipAs2(i+1,str1,str2)
    else:
        str2 = str2+ str1[i]
        return skipAs2(i+1,str1,str2)



def skipAs3(i,string):
    res = ""
    if i == len(string) -1:
        return string[i]
    if string[i] == "a":
        return skipAs3(i+1,string)
    else:
        res = string[i]
        res_from_below = skipAs3(i+1,string)
        res = res+res_from_below
        return res


def skipA4(string):
    res = ""
    if string == "":
        return string 
    if string[0] == "a":
        return skipA4(string[1::])
    else:
        res = string[0]
        ans_from_below = skipA4(string[1::])
        res = res+ans_from_below
        return res 

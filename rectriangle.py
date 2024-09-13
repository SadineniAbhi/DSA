def rectriangle(row,col):
    if row == 0:
        return
    if col>row:
        rectriangle(row-1,1)
        print()
    else:
        rectriangle(row,col+1)
        print("*",end = " ")
rectriangle(10,1)
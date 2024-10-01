name = "abhi"
for i in range(len(name)):
    for j in range(i,len(name)):
        for k in range(i,j+1):
            print(name[k],end=" ")
        print()

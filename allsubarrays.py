string = "abhijeeth"
count = 0
for i in range(len(string)):
    for j in range(i,len(string)):
        for k in range(i,j+1):
            print(string[k],end="")
        print()
    print()

print(count)
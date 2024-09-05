a = [1,2,3,4,5,6]
#generating all substring 

for i in range(len(a)):
      for j in range(i,len(a)):
            for k in range(i,j+1):
                  print(a[k],end = " ")
            print()	




    
    
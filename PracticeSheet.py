def checkbitonoroff(n,k):
	if n&(1<<k):
		print('True')
	else:
		print("falsd")
checkbitonoroff(5,1)

def icecreamParlor(m, arr):
    mapd = {}
    for i in range(len(arr)):
        mapd[arr[i]] = i 
    print(mapd)
    for j in range(len(arr)):
    	target = m-arr[j]
    	print(target)
    	if target in mapd:
    		return [i,mapd[i]]


for i in range(5):
	i = 0 
	j = 0 
	while 
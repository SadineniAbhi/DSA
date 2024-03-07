def filledrect(n,m):
	for i in range(n):
		for j in range(m):
			print("*",end = "")
		print()
def palpat(n):
	for i in range(n):
		for j in range(i):
			print(chr((ord('a'))+i),end="")
	print()

palpat(4)





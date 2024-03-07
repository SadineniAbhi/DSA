def my(*args):
	for i in args:
		print(i)


def new(**kargs):
	for i,j in kargs.items():
		print(i,j)

new(name="abhijeeth",age = 14)
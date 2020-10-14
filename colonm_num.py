x = int(input("Enter the no of rows : "))

for i in range(x):
	val = i+1
	dec = x-1
	for j in range(i+1):
		print(val,end="\t")
		val = val + dec
		dec = dec - 1
	print()

r = int(input("Enter the no of rows : "))
k=2
for row in range(1,r+1):
	for col in range(1,2*r):
		if (row+col == r+1) or (col - row == r-1) :
			print("*",end="")
		elif (row == r) and (col != k) :
			print("*",end="")
			k=k+2
		else:
			print(end=" ")
	print()

x = int(input("Enter the no of rows (it should be odd) : "))
k = (x//2)+3
for row in range(1,x+1):
	for col in range(1,2*x):
		if (col + row == x+1) or (col - row == x-1) :
			print("*",end="")
		elif (row == (x//2)+1) and (col == k) :
			print("*",end="")
			k = k+2
		else:
			print(end=" ")
	print()

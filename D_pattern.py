x = int(input("Enter no of rows : "))
k=1
l=1
for row in range(1,x+1):
	for col in range(1,x+1):
		if (col==2 and (row < x and row > 1)) or (col== x and row > 1 and row < x) :
			print("*",end="")
		elif (row == 1 and col == k):
			print("*",end="")
			k=k+2
		elif (row == x and col == l):
			print("*",end="")
			l=l+2
		else:
			print(end=" ")
	print()

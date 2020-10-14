for i in range(7):
	for j in range(5):
		if (i < 6 and (j == 0 or j == 4)) or (i == 6 and (j !=0 or j!=4)):
			print("*",end="")
		else:
			print(" ",end="")
	print() 

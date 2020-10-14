def heart(hight,width):
	mid = width//2
	for r in range(hight):
		for c in range(width):
			if (r == 0 and c % mid != 0) or (r == 1 and c % mid == 0) or (r - c == mid-1) or (r + c ==width+1) :
				print("*",end="")
			else:
				print(" ",end="")
		print()
x = int(input("Enter the highet of heart : "))
y = int(input("Enter the Width of heart : "))	
print("The Heart shape is :\n")
heart(x,y)

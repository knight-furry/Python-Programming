def fun(x):
	temp = 0
	for i in range(1,x+1):
		for j in range(i,x+1):
			for k in range(j,x+1):
				if k*k == i*i + j*j :
					print(i,j,k)
					temp = temp+1
	print ("The total no. of trikuths are: ",temp)
x = int(input("Enter the number upto get trikuth: "))
print("The Trikuth is:")
fun(x)

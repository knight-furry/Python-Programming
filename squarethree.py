def square(x):
	i=0
	while i*i <= x :
		j=0
		while j*j <= x :
			k=0
			while k*k <= x :
				if i*i+j*j+k*k == x :
					return True
				k=k+1
			j=j+1
		i=i+1
	return False
	
x = int(input("Enter any real number:"))
print(square(x))

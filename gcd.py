def gcd(m,n):
	fm=[]
	for i in range(1,m+1):
		if (m%i)==0:
			fm.append(i)
		
	fn=[]
	for j in range(1,n+1):
		if (n%j)==0:
			fn.append(j)
			
	fr=[]
	for f in fm:
		if f in fn:
			fr.append(f)
	return (fr[-1])	
			
x = 100
y = 90
z=gcd(x,y)
print(z)

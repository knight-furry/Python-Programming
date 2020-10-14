def prime(m):
	flag=0
	for i in range(1,m+1):
		if m%i == 0:
			flag=flag+1
	if flag==2:
		print("Num is Prime....!\n")
	else:
		print("Num is not Prime.....!\n")
		
print("Enter any number:")
x= int(input())
prime(x)

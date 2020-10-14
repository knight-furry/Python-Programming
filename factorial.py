def fun(n):
	if n==0:
		return 1
	else:
		return(n*fun(n-1))

print("Enter the number for factorial:")
x=int(input())
y=fun(x)
print("Factorial is:")
print(y)

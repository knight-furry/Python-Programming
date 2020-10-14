def cal(x):
	temp = x
	count = total = 0
	m=1
	while temp != 0:
		temp=temp//10
		count=count+1
		m = m*10
	while x != 0:
		rem=x%10
		m=m//10
		total = total + (m*rem)
		x=x//10
	return total
print("Enetr a number:")
x = int(input())
print("Reverse number is :")
print(cal(x))

def cal(x):
	temp = x
	count = total = 0
	m=n=1
	while temp != 0:
		temp=temp//10
		count=count+1
		m = m*10
	m = m//10
	while x != 0:
		rem=x%10
		total = total + (m*rem)
		z = (m*rem)-rem
		m = 10*n
		n = n*10
		x=x//10
		
	return (total-z)
print("Enetr a number:")
x = int(input())
print("The swaped of last and first digit of a number is :")
print(cal(x))

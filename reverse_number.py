def reverse(x):
	sum = 0
	while x != 0:
		rem = x%10
		sum = sum * 10 + rem
		x = x//10
	return sum
x = int(input("Enter a number to reverse it: "))
print("The Reverse number is: ",reverse(x))

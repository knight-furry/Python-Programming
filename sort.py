x = int(input("Enter the size of list: "))
l = []
for i in range(x):
	a = int(input("Enter element: "))
	l.append(a)
print("The given list is: ",l)
l.sort()
print("The sorted list is: ",l)

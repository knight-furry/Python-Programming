def insertion(l):
	for start in range(len(l)):
		pos = start
		while pos > 0 and l[pos] <l[pos - 1]:
			(l[pos],l[pos - 1]) = (l[pos - 1],l[pos])
			pos = pos - 1
	return (l)
n = int(input("Enter the size of list:"))
l = []
for i in range(0,n):
	item = int(input("Enter element: "))
	l.append(item)
print("The given list is:",l)
print("Now the sorted list is:",insertion(l))

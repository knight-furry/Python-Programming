def selection(l):
	for start in range(len(l)):
		minpos = start
		for i in range(start,len(l)):
			if l[i] < l[minpos]:
				minpos = i
		(l[start],l[minpos]) = (l[minpos],l[start])
	return (l)
n = int(input("Enter the size of list:"))
l = []
for i in range(0,n):
	item = int(input("Enter element: "))
	l.append(item)
print("The given list is:",l)
print("Now the sorted list is:",selection(l))

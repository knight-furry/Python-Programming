def even_sort(l):
	for i in range(len(l)):
		pos = i
		for j in range(i,len(l)):
			if l[i]%2 == 0 and l[j] == 0 :
				if l[pos] < l[j] :
					temp = l[pos]
					l[pos] = l[j]
					l[j] = temp
	return l

x = int(input("Enter the size of list: "))
l = []
for i in range(x):
	a = int(input("Enter element: "))
	l.append(a)
print("The given list is: ",l)

print("The even sorted list is: ",even_sort(l))

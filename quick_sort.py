def quicksort(a,low,high):
	if high - low <=1:
		return ()
	y = low+1
	for g in range(low+1,high):
		if a[g] <= a[low]:
			(a[y],a[g]) = (a[g],a[y])
			y=y+1
	(a[low],a[y-1]) = (a[y-1],a[low])
	quicksort(a,low,y-1)
	quicksort(a,y,high)
	return (a)

n = int(input("Enter the size of list:"))
l = []
for i in range(0,n):
	item = int(input("Enter element: "))
	l.append(item)
print("The given list is:",l)
print("Now the sorted list is:",quicksort(l,0,n))

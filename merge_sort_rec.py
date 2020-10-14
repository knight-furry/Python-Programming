def merge(a,b):
	(c,m,n) = ([],len(a),len(b))
	i=j=0;
	while (i+j) < (m+n):
		if i == m:
			c.append(b[j])
			j=j+1
		elif j == n:
			c.append(a[i])
			i=i+1
		elif a[i] <= b[j]:
			c.append(a[i])
			i=i+1
		elif a[i] > b[j]:
			c.append(b[j])
			j=j+1
	return (c)

def mergesort(l,left,right):
	L=R=[]
	if right - left <=1:
		return (l[left])
	if right - left > 1:
		mid = (left+right) // 2
		L = mergesort(l,left,mid)
		R = mergesort(l,mid,right)
		return (merge(L,R))

n = int(input("Enter the size of list:"))
l = []
for i in range(0,n):
	item = int(input("Enter element: "))
	l.append(item)
print("The given list is:",l)
print("Now the sorted list is:",mergesort(l,0,n))

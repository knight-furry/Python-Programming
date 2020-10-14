def binarysearch(l,x,low,high):
	if (high-low == 0):
		return False
	mid = (high+low)//2
	if (x == l[mid]):
		return True
	if (x < l[mid]):
		return(binarysearch(l,x,low,mid))
	else:
		return(binarysearch(l,x,mid+1,high))
n = int(input("Enter the size of list:"))
l = []
for i in range(0,n):
	item = int(input("Enter element: "))
	l.append(item)
print("The given list is:",l)
print("Now Enter the element to be found:")
x = int(input())
z = binarysearch(l,x,0,n)
if z == True:
	print("The Element is founded....!\n")
else:
	print("The element NOT founded.....!\n")

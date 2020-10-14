def demo(m):
	x=[]
	sum1=sum2=0
	for i in l:
		if i%2 == 0:
			sum1=sum1+(i**2)
		else:
			sum2=sum2+(i**2)
	x=[sum1,sum2]
	return x

print("enter size of list:")
l = []
x=int(input())
print("Enter the elements:")
for i in range(x):
	y=int(input())
	l.append(y)
print("your list is:")
print(l)
print("your output is:")
print(demo(l))

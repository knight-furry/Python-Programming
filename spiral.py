x = int(input("Enter the no of rows : "))
l = [[0 for i in range(x)] for j in range(x)]
mid = (x+1)//2
num = 1
low = 0
high = x-1

for i in range(mid):
	for j in range(low,high+1):
		l[low][j] = num
		num = num + 1
	for j in range(low+1,high+1):
		l[j][high] = num
		num = num + 1
	for j in range(high-1,low-1,-1):
		l[high][j] = num
		num = num + 1
	for j in range(high-1,low,-1):
		l[j][low] = num
		num = num + 1
	low = low + 1
	high = high -1

for i in range(x):
	for j in range(x):
		print(l[i][j],end="\t")
	print()

x = int(input("Enter the no of columns : "))
n = x // 2
name = input("Enter any name : ")
name = name.upper()
l = len(name)

for i in range(n) :
	for j in range(n-i-1) :
		print(" ",end="")
	for j in range(i+1) : 
		print("* ",end="")
	if x%2 == 0 :
		for j in range(2*(n-i-1)) :
			print(" ",end="")
	else :
		for j in range(2*(n-i-1)+1) :
			print(" ",end="")
	for j in range(i+1) : 
		print("* ",end="")
	print()

if x%2 == 0:
	if l%2 == 0:
		print("* "* ((x-l)//2) + " ".join(name) + " *"*((x-l)//2))
	else:
		print("* "* ((x-l)//2) + " ".join(name) + " *"*(((x-l)//2)+1))
else:
	if l%2 == 0:
		print("* "* ((x-l)//2) + " ".join(name) + " *"*(((x-l)//2)+1))
	else:
		print("* "* ((x-l)//2) + " ".join(name) + " *"*((x-l)//2))

for i in range(x,0,-1) :
#	print(" "*(x-i) + "* "*(i))
	for j in range(x-i) :
		print(" ",end="")
	for j in range(i,0,-1) :
		print("* ",end="")
	print()

num = input("Enter the odd digit number : ")
length = len(num)
if length % 2 != 0 :
	for i in range(length):
		for j in range(length):
			if i==j or i+j==length-1 :
				print (num[i],end=" ")
			else:
				print (" ",end=" ")
		print ()
else:
	print ("The number is NOT odd digit......!")

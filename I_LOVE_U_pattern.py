list1 = [[" " for i in range(7)] for j in range(6)]
list2 = [[" " for i in range(7)] for j in range(6)]
list3 = [[" " for i in range(7)] for j in range(6)]

for row in range(6):
	for col in range(7):
		if (row == 0 or row ==5 or col == 3) :
			list1[row][col] = "*"

for row in range(6):
	for col in range(7):
		if (row == 0 and (col != 0 and col != 3 and col != 6)) or (row == 1 and (col == 0 or col == 3 or col == 6)) or (row - col == 2) or (row + col == 8) :
			list2[row][col] = "*"

for row in range(6):
	for col in range(7):
		if ((col == 0 or col == 6) and row != 5) or (row == 5 and col != 0 and col != 6) :
			list3[row][col] = "*"
			
# Code to print name
print("\n######################################################################\n")
for i in range(6):
	for j in range(7):
		print(list1[i][j],end=" ")
	print(end="  ")
	for j in range(7):
		print(list2[i][j],end=" ")
	print(end="  ")
	for j in range(7):
		print(list3[i][j],end=" ")
	print()
print("\n######################################################################\n")

list1 = [[" " for i in range(6)] for j in range(6)]
list2 = [[" " for i in range(6)] for j in range(6)]

# code for N:
for row in range(6):
	for col in range(6):
		if col == 0 or col == 5 or row == col :
			list1[row][col] = "*"

# code for O:
for row in range(6):
	for col in range(6):
		if ((col == 0 or col == 5) and (row != 0 and row != 5)) or ((row == 0 or row == 5) and (col != 0 and col != 5))  :
			list2[row][col] = "*"

for i in range(6):
	for j in range(6):
		print(list1[i][j],end=" ")
	print(end=" ")
	for j in range(6):
		print(list2[i][j],end=" ")
	print()

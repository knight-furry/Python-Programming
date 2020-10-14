list1 = [[" " for i in range(6)] for j in range(6)]
list2 = [[" " for i in range(6)] for j in range(6)]
list3 = [[" " for i in range(6)] for j in range(6)]
list4 = [[" " for i in range(6)] for j in range(6)]
list5 = [[" " for i in range(6)] for j in range(6)]
list6 = [[" " for i in range(6)] for j in range(6)]
list7 = [[" " for i in range(6)] for j in range(6)]
list8 = [[" " for i in range(6)] for j in range(6)]
list9 = [[" " for i in range(6)] for j in range(6)]
list10 = [[" " for i in range(6)] for j in range(6)]
# code for G
for row in range(6):
	for col in range(6):
		if (row == 0 and (col != 0 and col != 5 and col != 4)) or (col == 0 and (row != 0 and row != 5)) or (row == 5 and (col != 0 and col != 4)) or (col == 4 and (row != 0 and row != 2 and row != 5)) or (col == 5 and row > 2) or (row ==3 and col == 3) :
			list1[row][col] = "*"
# code for O
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or ((col == 0 or col == 5) and (row != 0 and row != 5)) :
			list2[row][col] = "*"

# code for C
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or (col == 0 and (row != 0 and row != 5)) or (col == 5 and (row == 1 or row == 4)) :
			list3[row][col] = "*"
# code for O
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or ((col == 0 or col == 5) and (row != 0 and row != 5)) :
			list4[row][col] = "*"
# code for R
for row in range(6):
	for col in range(6):
		if col == 0 or (col == 5 and (row !=0 and row != 3)) or ((row == 0 or row == 3) and col != 5) :
			list5[row][col] = "*"
# code for O
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or ((col == 0 or col == 5) and (row != 0 and row != 5)) :
			list6[row][col] = "*"
# code for N
for row in range(6):
	for col in range(6):
		if col == 0 or col == 5 or col == row :
			list7[row][col] = "*"
# code for A
for row in range(6):
	for col in range(6):
		if ((col == 0 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 5)) :
			list8[row][col] = "*"
# code for G
for row in range(6):
	for col in range(6):
		if (row == 0 and (col != 0 and col != 5 and col != 4)) or (col == 0 and (row != 0 and row != 5)) or (row == 5 and (col != 0 and col != 4)) or (col == 4 and (row != 0 and row != 2 and row != 5)) or (col == 5 and row > 2) or (row ==3 and col == 3) :
			list9[row][col] = "*"
# code for O
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or (col == 0 or col == 5) and (row != 0 and row != 5) :
			list10[row][col] = "*"
			
# Code to print name
print("\n##############################################################################################################################################\n")
for i in range(6):
	for j in range(6):
		print(list1[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list2[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list3[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list4[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list5[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list6[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list7[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list8[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list9[i][j],end=" ")
	print(end="  ")
	for j in range(6):
		print(list10[i][j],end=" ")
	print()
print("\n##############################################################################################################################################\n")

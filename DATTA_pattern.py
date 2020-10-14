# Print the DATTA name
list1 = [[" " for i in range(5)] for j in range(6)]
list2 = [[" " for i in range(5)] for j in range(6)]
list3 = [[" " for i in range(5)] for j in range(6)]
list4 = [[" " for i in range(5)] for j in range(6)]
list5 = [[" " for i in range(5)] for j in range(6)]

# code for D
for row in range(6):
	for col in range(5):
		if ((row == 0 or row == 5) and (col < 4)) or (col == 1 or col == 4) and (row != 0 and row != 5) :
			list1[row][col] = "*"

# code for A
for row in range(6):
	for col in range(5):
		if ((col == 0 or col ==4) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 4)) :
			list2[row][col] = "*"

# code for T
for row in range(6):
	for col in range(5):
		if row == 0 or col == 2 :
			list3[row][col] = "*"

# code for T
for row in range(6):
	for col in range(5):
		if row == 0 or col == 2 :
			list4[row][col] = "*"

# code for A
for row in range(6):
	for col in range(5):
		if ((col == 0 or col ==4) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 4)) :
			list5[row][col] = "*"
			
# Code to print name
print("\n######################################################################\n")
for i in range(6):
	for j in range(5):
		print(list1[i][j],end=" ")
	print(end="  ")
	for j in range(5):
		print(list2[i][j],end=" ")
	print(end="  ")
	for j in range(5):
		print(list3[i][j],end=" ")
	print(end="  ")
	for j in range(5):
		print(list4[i][j],end=" ")
	print(end="  ")
	for j in range(5):
		print(list5[i][j],end=" ")
	print()
print("\n######################################################################\n")

def pattern(name):
	list1 = []
	for i in name :
		if i == "A" :
			list_a = [[" " for i in range(6)] for j in range(6)]
			# code for A
			for row in range(6):
				for col in range(6):
					if ((col == 0 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 5)) :
						list_a[row][col] = "*"
			list1.append(list_a)
		elif i == "B" :
			list_b = [[" " for i in range(6)] for j in range(6)]
			# code for B
			for row in range(6):
				for col in range(6):
					if col == 0 or (col == 5 and (row !=0 and row != 3 and row != 5)) or ((row == 0 or row == 3 or row == 5) and col != 5) :
						list_b[row][col] = "*"
			list1.append(list_b)
		elif i == "C" :
			list_c = [[" " for i in range(6)] for j in range(6)]
			# code for C
			for row in range(6):
				for col in range(6):
					if ((row == 0 or row == 5) and (col != 0 and col != 5)) or (col == 0 and (row != 0 and row != 5)) or (col == 5 and (row == 1 or row == 4)) :
						list_c[row][col] = "*"
			list1.append(list_c)
		elif i == "D" :
			list_d = [[" " for i in range(6)] for j in range(6)]
			# code for D
			for row in range(6):
				for col in range(6):
					if ((row == 0 or row == 5) and (col < 5)) or (col == 1 or col == 5) and (row != 0 and row != 5) :
						list_d[row][col] = "*"
			list1.append(list_d)
		elif i == "E" :
			list_e = [[" " for i in range(6)] for j in range(6)]
			# code for E
			for row in range(6):
				for col in range(6):
					if col == 0 or row == 0 or row == 2 or row == 5 :
						list_e[row][col] = "*"
			list1.append(list_e)
		elif i == "F" :
			list_f = [[" " for i in range(6)] for j in range(6)]
			# code for F
			for row in range(6):
				for col in range(6):
					if col == 0 or row == 0 or row == 3 :
						list_f[row][col] = "*"
			list1.append(list_f)
		elif i == "G" :
			list_g = [[" " for i in range(6)] for j in range(6)]		
			# code for G
			for row in range(6):
				for col in range(6):
					if (row == 0 and (col != 0 and col != 5 and col != 4)) or (col == 0 and (row != 0 and row != 5)) or (row == 5 and (col != 0 and col != 4)) or (col == 4 and (row != 0 and row != 2 and row != 5)) or (col == 5 and row > 2) or (row ==3 and col == 3) :
						list_g[row][col] = "*"
			list1.append(list_g)
		elif i == "H" :
			list_h = [[" " for i in range(6)] for j in range(6)]
			# code for H
			for row in range(6) :
				for col in range(6):
					if col == 0 or col == 5 or row == 3 :
						list_h[row][col] = "*"
			list1.append(list_h)
		elif i == "I" :
			list_i = [[" " for i in range(6)] for j in range(6)]
			# code for I
			for row in range(6):
				for col in range(6):
					if row == 0 or row == 5 or col == 3 :
						list_i[row][col] = "*"
			list1.append(list_i)
		elif i == "J" :
			list_j = [[" " for i in range(6)] for j in range(6)]
			# code for J
			for row in range(6):
				for col in range(6):
					if row == 0 or (col == 3 and row != 5) or (row == 5 and col < 3) :
						list_j[row][col] = "*"
			list1.append(list_j)
		elif i == "K" :
			list_k = [[" " for i in range(6)] for j in range(6)]
			# code for K
			for row in range(6):
				for col in range(6):
					if col == 0 or (col + row == 3) or (row - col == 1) :
						list_k[row][col] = "*"
			list1.append(list_k)
		elif i == "L" :
			list_l = [[" " for i in range(6)] for j in range(6)]	
			# code for L
			for row in range(6):
				for col in range(6):
					if col == 0 or row ==5 :
						list_l[row][col] = "*"
			list1.append(list_l)
		elif i == "M" :
			list_m = [[" " for i in range(6)] for j in range(6)]
			# code for M
			for row in range(6):
				for col in range(6):
					if col == 0 or col == 5 or (col == row and col < 3) or (col + row == 5 and col > 2) :
						list_m[row][col] = "*"
			list1.append(list_m)
		elif i == "N" :
			list_n = [[" " for i in range(6)] for j in range(6)]
			# code for N
			for row in range(6):
				for col in range(6):
					if col == 0 or col == 5 or col == row :
						list_n[row][col] = "*"
			list1.append(list_n)
		elif i == "O" :
			list_o = [[" " for i in range(6)] for j in range(6)]
			# code for O
			for row in range(6):
				for col in range(6):
					if ((row == 0 or row == 5) and (col != 0 and col != 5)) or ((col == 0 or col == 5) and (row != 0 and row != 5)) :
						list_o[row][col] = "*"
			list1.append(list_o)
		elif i == "P" :
			list_p = [[" " for i in range(6)] for j in range(6)]
			# code for P
			for row in range(6):
				for col in range(6):
					if col == 0 or (col == 5 and (row == 1 or row == 2)) or ((row == 0 or row == 3) and col != 5) :
						list_p[row][col] = "*"
			list1.append(list_p)
		elif i == "Q" :
			list_q = [[" " for i in range(6)] for j in range(6)]
			# code for Q
			for row in range(6):
				for col in range(6):
					if ((row == 0 or row == 5) and (col != 0 and col != 5)) or ((col == 0 or col == 5) and (row != 0 and row != 5)) or (col == row and col > 2) :
						list_q[row][col] = "*"
			list1.append(list_q)
		elif i == "R" :		
			list_r = [[" " for i in range(6)] for j in range(6)]
			# code for R
			for row in range(6):
				for col in range(6):
					if col == 0 or (col == 5 and (row !=0 and row != 3)) or ((row == 0 or row == 3) and col != 5) :
						list_r[row][col] = "*"
			list1.append(list_r)
		elif i == "S" :	
			list_s = [[" " for i in range(6)] for j in range(6)]
			# code for S
			for row in range(6):
				for col in range(6):
					if (col == 0 and (row == 1 or row == 2)) or (col == 5 and (row == 1 or row == 4)) or ((row == 0 or row == 3 or row == 5) and (col != 0 and col != 5)) or (col == 0 and row == 5) :
						list_s[row][col] = "*"
			list1.append(list_s)
		elif i == "T" :
			list_t = [[" " for i in range(6)] for j in range(6)]
			# code for T
			for row in range(6):
				for col in range(6):
					if row == 0 or col == 3 :
						list_t[row][col] = "*"
			list1.append(list_t)
		elif i == "U" :
			list_u = [[" " for i in range(6)] for j in range(6)]
			# code for U
			for row in range(6):
				for col in range(6):
					if ((col == 0 or col == 5) and row != 5) or (row == 5 and col != 0 and col != 5) :
						list_u[row][col] = "*"
			list1.append(list_u)
		elif i == "V" :
			list_v = [[" " for i in range(6)] for j in range(6)]
			# code for V
			for row in range(6):
				for col in range(6):
					if (row - col == 3) or (row + col == 8) or ((col == 0 or col == 5) and row < 4) :
						list_v[row][col] = "*"
			list1.append(list_v)
		elif i == "W" :	
			list_w = [[" " for i in range(6)] for j in range(6)]
			# code for W
			for row in range(6):
				for col in range(6):
					if col == 0 or col == 5 or (col == row and col > 2) or (col + row == 5 and col < 3) :
						list_w[row][col] = "*"
			list1.append(list_w)
		elif i == "X" :
			list_x = [[" " for i in range(6)] for j in range(6)]
			# code for X
			for row in range(6):
				for col in range(6):
					if col == row or col + row == 5  :
						list_x[row][col] = "*"
			list1.append(list_x)
		elif i == "Y" :	
			list_y = [[" " for i in range(6)] for j in range(6)]
			# code for Y
			for row in range(6):
				for col in range(6):
					if ((col == row) and row < 3) or col + row == 5 :
						list_y[row][col] = "*"
			list1.append(list_y)
		elif i == "Z" :	
			list_z = [[" " for i in range(6)] for j in range(6)]
			# code for Z
			for row in range(6):
				for col in range(6):
					if (col + row == 5) or row == 0 or row == 5 :
						list_z[row][col] = "*"
			list1.append(list_z)
		elif i == " " :
			list_space = [[" " for i in range(6)] for j in range(6)]
			list1.append(list_space)
		else:
			print("Invalid name.....!")
	return list1

print("\n******** Welcome to star pattern programm *********\n")
name = input("Enter any name : ")
name = name.upper()
result = pattern(name)
print("\n####################################################################################################################################################\n")
for i in range(6) :
	for j in range(len(result)) :
		for k in range(6) :
			print(result[j][i][k],end=" ")
		print(end="  ")
	print()
print("\n######################################################################################################################################################\n")

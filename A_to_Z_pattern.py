list_a = [[" " for i in range(6)] for j in range(6)]
list_b = [[" " for i in range(6)] for j in range(6)]
list_c = [[" " for i in range(6)] for j in range(6)]
list_d = [[" " for i in range(6)] for j in range(6)]
list_e = [[" " for i in range(6)] for j in range(6)]
list_f = [[" " for i in range(6)] for j in range(6)]
list_g = [[" " for i in range(6)] for j in range(6)]
list_h = [[" " for i in range(6)] for j in range(6)]
list_i = [[" " for i in range(6)] for j in range(6)]
list_j = [[" " for i in range(6)] for j in range(6)]
list_k = [[" " for i in range(6)] for j in range(6)]
list_l = [[" " for i in range(6)] for j in range(6)]
list_m = [[" " for i in range(6)] for j in range(6)]
list_n = [[" " for i in range(6)] for j in range(6)]
list_o = [[" " for i in range(6)] for j in range(6)]
list_p = [[" " for i in range(6)] for j in range(6)]
list_q = [[" " for i in range(6)] for j in range(6)]
list_r = [[" " for i in range(6)] for j in range(6)]
list_s = [[" " for i in range(6)] for j in range(6)]
list_t = [[" " for i in range(6)] for j in range(6)]
list_u = [[" " for i in range(6)] for j in range(6)]
list_v = [[" " for i in range(6)] for j in range(6)]
list_w = [[" " for i in range(6)] for j in range(6)]
list_x = [[" " for i in range(6)] for j in range(6)]
list_y = [[" " for i in range(6)] for j in range(6)]
list_z = [[" " for i in range(6)] for j in range(6)]

# code for A
for row in range(6):
	for col in range(6):
		if ((col == 0 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 5)) :
			list_a[row][col] = "*"

# code for B
for row in range(6):
	for col in range(6):
		if col == 0 or (col == 5 and (row !=0 and row != 3 and row != 5)) or ((row == 0 or row == 3 or row == 5) and col != 5) :
			list_b[row][col] = "*"

# code for C
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or (col == 0 and (row != 0 and row != 5)) or (col == 5 and (row == 1 or row == 4)) :
			list_c[row][col] = "*"

# code for D
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col < 5)) or (col == 1 or col == 5) and (row != 0 and row != 5) :
			list_d[row][col] = "*"

# code for E
for row in range(6):
	for col in range(6):
		if col == 0 or row == 0 or row == 2 or row == 5 :
			list_e[row][col] = "*"

# code for F
for row in range(6):
	for col in range(6):
		if col == 0 or row == 0 or row == 3 :
			list_f[row][col] = "*"

# code for G
for row in range(6):
	for col in range(6):
		if (row == 0 and (col != 0 and col != 5 and col != 4)) or (col == 0 and (row != 0 and row != 5)) or (row == 5 and (col != 0 and col != 4)) or (col == 4 and (row != 0 and row != 2 and row != 5)) or (col == 5 and row > 2) or (row ==3 and col == 3) :
			list_g[row][col] = "*"

# code for H
for row in range(6):
	for col in range(6):
		if col == 0 or col == 5 or row == 3 :
			list_h[row][col] = "*"

# code for I
for row in range(6):
	for col in range(6):
		if row == 0 or row == 5 or col == 3 :
			list_i[row][col] = "*"

# code for J
for row in range(6):
	for col in range(6):
		if row == 0 or (col == 3 and row != 5) or (row == 5 and col < 3) :
			list_j[row][col] = "*"

# code for K
for row in range(6):
	for col in range(6):
		if col == 0 or (col + row == 3) or (row - col == 1) :
			list_k[row][col] = "*"

# code for L
for row in range(6):
	for col in range(6):
		if col == 0 or row ==5 :
			list_l[row][col] = "*"

# code for M
for row in range(6):
	for col in range(6):
		if col == 0 or col == 5 or (col == row and col < 3) or (col + row == 5 and col > 2) :
			list_m[row][col] = "*"

# code for N
for row in range(6):
	for col in range(6):
		if col == 0 or col == 5 or col == row :
			list_n[row][col] = "*"

# code for O
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or ((col == 0 or col == 5) and (row != 0 and row != 5)) :
			list_o[row][col] = "*"

# code for P
for row in range(6):
	for col in range(6):
		if col == 0 or (col == 5 and (row == 1 or row == 2)) or ((row == 0 or row == 3) and col != 5) :
			list_p[row][col] = "*"

# code for Q
for row in range(6):
	for col in range(6):
		if ((row == 0 or row == 5) and (col != 0 and col != 5)) or ((col == 0 or col == 5) and (row != 0 and row != 5)) or (col == row and col > 2) :
			list_q[row][col] = "*"

# code for R
for row in range(6):
	for col in range(6):
		if col == 0 or (col == 5 and (row !=0 and row != 3)) or ((row == 0 or row == 3) and col != 5) :
			list_r[row][col] = "*"

# code for S
for row in range(6):
	for col in range(6):
		if (col == 0 and (row == 1 or row == 2)) or (col == 5 and (row == 1 or row == 4)) or ((row == 0 or row == 3 or row == 5) and (col != 0 and col != 5)) or (col == 0 and row == 5) :
			list_s[row][col] = "*"

# code for T
for row in range(6):
	for col in range(6):
		if row == 0 or col == 3 :
			list_t[row][col] = "*"

# code for U
for row in range(6):
	for col in range(6):
		if ((col == 0 or col == 5) and row != 5) or (row == 5 and col != 0 and col != 5) :
			list_u[row][col] = "*"

# code for V
for row in range(6):
	for col in range(6):
		if (row - col == 3) or (row + col == 8) or ((col == 0 or col == 5) and row < 4) :
			list_v[row][col] = "*"

# code for W
for row in range(6):
	for col in range(6):
		if col == 0 or col == 5 or (col == row and col > 2) or (col + row == 5 and col < 3) :
			list_w[row][col] = "*"

# code for X
for row in range(6):
	for col in range(6):
		if col == row or col + row == 5  :
			list_x[row][col] = "*"

# code for Y
for row in range(6):
	for col in range(6):
		if ((col == row) and row < 3) or col + row == 5 :
			list_y[row][col] = "*"

# code for Z
for row in range(6):
	for col in range(6):
		if (col + row == 5) or row == 0 or row == 5 :
			list_z[row][col] = "*"

# Code to print name
print("\n##############################################################################################################################################\n")
for i in range(6):
	for j in range(6):
		print(list_z[i][j],end=" ")
	print(end="  ")
	print()
print("\n##############################################################################################################################################\n")

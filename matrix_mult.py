r1 = int(input("Enter the no of rows for matrix 1: "))
c1 = int(input("Enter the no of columns for matrix 1: "))
print("Enter elements in matrix1 : ")
matrix1 = [[int(input()) for i in range(r1)] for j in range(c1)]
r2 = int(input("Enter the no of rows for matrix 2: "))
c2 = int(input("Enter the no of columns for matrix 2: "))
print("Enter elements in matrix2 : ")
matrix2 = [[int(input()) for i in range(r2)] for j in range(c2)]

print("\nThe given matrix1 is : ")
for i in range(r1):
	for j in range(c1):
		print(format(matrix1[i][j]),end="\t")
	print()
print("\nThe given matrix2 is : ")
for i in range(r2):
	for j in range(c2):
		print(format(matrix2[i][j]), end="\t")
	print()

if c1 == r2 :
	result = [[0 for i in range(r2)] for j in range(c1)]
	print("\nThe Multiplication of two matrices is : ")
	for i in range(r1):
		for j in range(c2):
			for k in range(c1):
				result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]
	for i in range(r2):
		for j in range(c1):
			print(format(result[i][j]), end="\t")
		print()
	print()
else:
	print("Matrix multiplication NOT possible......!\n")

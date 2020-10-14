r = int(input("Enter the no of rows : "))
c = int(input("Enter the no of columns : "))
print("Enter elements in matrix1 : ")
matrix1 = [[int(input()) for i in range(r)] for j in range(c)]
print("\nThe given matrix is : ")
for i in range(r):
	for j in range(c):
		print(format(matrix1[i][j]), end="\t")
	print()

print("Enter elements in matrix2 : ")
matrix2 = [[int(input()) for i in range(r)] for j in range(c)]
print("\nThe given matrix2 is : ")
for i in range(r):
	for j in range(c):
		print(format(matrix2[i][j]), end="\t")
	print()
	
result = [[0 for i in range(r)] for j in range(c)]
print("\nThe Addition of two matrices is : ")
for i in range(r):
	for j in range(c):
		result[i][j] = matrix1[i][j] + matrix2[i][j]

for i in range(r):
	for j in range(c):
		print(format(result[i][j]), end="\t")
	print()
print()

def initialize(board,n) :
	for key in ["queen","row","col","rwtose","swtone"]:
		board[key] = {}
	for i in range(n):
		board["queen"][i] = -1
		board["row"][i] = 0
		board["col"][i] = 0
	for i in range(-(n-1),n):
		board["rwtose"][i] = 0
	for i in range(2*n-1):
		board["swtone"][i] = 0

def printboard(board):
	for row in sorted(board["queen"].keys()):
		print((row,board["queen"][row]),end=" ")
	print()

def frees(i,j,board):
	return(board["row"][i] == 0 and board["col"][j] == 0 and board["rwtose"][j-i] == 0 and board["swtone"][j+i] == 0)

def addqueen(i,j,board):
	board["queen"][i] = j
	board["row"][i] = 1
	board["col"][j] = 1
	board["rwtose"][j-i] = 1
	board["swtone"][j+i] = 1

def undoqueen(i,j,board):
	board["queen"][i] = -1
	board["row"][i] = 0
	board["col"][j] = 0
	board["rwtose"][j-i] = 0
	board["swtone"][j+i] = 0

def placequeen(i,board):
	n = len(board["queen"].keys())
	for j in range(n):
		if frees(i,j,board):
			#return True
			addqueen(i,j,board)
			if i == n-1:
				#printboard(board)
				return True
			else:
				extendsoln = placequeen(i+1,board)
			if extendsoln :
				return (True)
			else:
				undoqueen(i,j,board)
	else:
			return False

board = {}
n = int(input("Enter how many queens required...!\n"))
initialize(board,n)
if placequeen(0,board):
	printboard(board)

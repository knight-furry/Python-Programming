def fun():
	name = input("What is your name: ")
	add  = input("Enter your address: ")
	col = input("What is your college name: ")
	branch = input("Enter your Branch name: ")
	year = input("Enter your acadmic year: ")
	roll = int(input("What is your roll number: "))
	mobile = int(input("Enter your mobile number: "))
	mark = input("Enter your percentage mark: ")
	print("\n**************************************STUDENT BIODATA*************************************\n")
	print("Rollno.\tName\tAddress\tCollege Name\tBranch\tAcadmic year\tMobileno.\tMark")
	print(roll,"\t",name,"\t",add,"\t",col,"\t",branch,"\t",year,"\t\t",mobile,"\t",mark,"\n")

fun()

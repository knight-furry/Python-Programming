def fornumber():
	while (True):
	try:
		x = int(input("Enter the valid Number without any charactor:"))
	except ValueError:
		print("Invalid intger type....!")
	else:
		break
#####################################
def forstring():
	while (True):
	try:
		x = (input("Enter the valid string without any number:"))
	except NameError:
		print("Invalid name type....!")
	else:
		break
#######################################
print("Two types of error:\n1.number error\n2.name error")
x  = int(input("Enter your choice:"))
while x !=0:
	if x==1:
		fornumber()
	elif x==2:
		forstring()
	x=int(input("Do you want to continue(if no enter 0):"))

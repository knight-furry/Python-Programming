import random
value = 0
count = 0
while value != " " :
	if count % 2 == 0 :
		value = input("player1 : ")
		value = random.randint(1,6)
		print(value)
	else:
		value = input("player2 : ")
		value = random.randint(1,6)
		print(value)
	count = count + 1
	value = input("Do you want to play(y/n) : ")
	if value == 'n' :
		value = " "

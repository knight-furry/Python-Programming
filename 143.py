print("\n########################################\n")
for i in range(6):
	for j in range(19):
		if (i==0 and (j!=5 and j!=6 and j!=9 and j!=12 and j!=13 and j!=15 and j!=16 and j!=17)) or (i==1 and (j==6 or j==9 or j==12 or j==14 or j==18)) or (j==2) or (i==2 and (j==6 or j==12 or j==14 or j==18)) or (i==5 and (j<5 or j==9 or j==15 or j==16 or j==17)) or (i==3 and (j==7 or j==11 or j==14 or j==18)) or (i==4 and (j==8 or j==10 or j==14 or j==18)):
			print("*",end="")
		else:
			print(" ",end="")
	print()
print("\n########################################\n")

def remdup(l):
	dup=[]
	for i in l:
		if i not in dup:
			dup.append(i) 
	return(dup)

l=[2,4,5,8,5,2,1]
y=[]
y=remdup(l)
print(y)

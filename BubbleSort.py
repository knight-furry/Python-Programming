def Bsort(seq):
	for i in range(len(seq)-1):
		for j in range(len(seq)-i-1):
			if seq[j] > seq[j+1] :
				(seq[j],seq[j+1]) = (seq[j+1],seq[j])
	return seq
seq = [74,32,89,55,21,64]
print("The sorted list is : ", Bsort(seq))

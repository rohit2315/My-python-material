n=int(input('Enter the num:'))
for i in range(n):
	for j in range(i+1):
		x=0
		for k in range(j):
			x=x+n-k
		if j%2==0:
			print(x+i+1-j,end=' ')
		else:
			print(x+n-i,end=' ')
	print()	
				
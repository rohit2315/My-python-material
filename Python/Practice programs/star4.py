def diamond(rows):
	for i in range(1,rows):
		print(' '*rows-i-1+' *'*i)
	for j in range(rows-1,0,-1):
		print(' '*rows-j+' *'*j)

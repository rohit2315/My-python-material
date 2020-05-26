n=int(input('Enter the num:'))
for i in range(n):
	val=i+1
	dec=n-1

	
	for j in range(i+1):
		print(format(val,' '),end='')
		val=val+dec
		dec-1
	print()	
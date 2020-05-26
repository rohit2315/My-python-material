string=input('Enter string:')
for i in range(len(string)):
	for j in range(i+1):
		print(string[j],end='')
	print()	                    # it means new line
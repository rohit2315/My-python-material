n=input():
i=1
j=2
for i in range(1,n+1):
	if i<=n:
		print('*')
		i+=1
for j in range(1,n+1):
	if j<=n:
		print('*'*(i-1))
		j+=1



import random
num=random.randint(1,100)

lis_count=0
while lis_count<6:
	guess=int(input('Enter the num:'))
	lis_count+=1
	if guess<num:
		print('Guess is too low')
	elif guess>num:
	    print('Guess is too high')
	elif guess==num:
	    break
if guess==num:
	print(f'You guessed the num in {lis_count} attempt')
if guess!=num:
    print(f'Nope the correct num is {num} ')	


	



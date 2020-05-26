correct_word='Rahul'
Guess=''
Guess_count=0
Guess_limit=3
out_of_guess=False

while Guess!=correct_word and not out_of_guess:

		
	if Guess_count<Guess_limit:
		Guess=input('Enter the Guess:')
		Guess_count+=1


	else:
		out_of_guess=True

if out_of_guess:
	print('You loose')
else:
	print('You win')
	    	
			
		     	


		
	
	     	


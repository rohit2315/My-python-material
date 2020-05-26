for i in range(6):
	if i==0 or i==6-1:
		print('*'*6)
	else:
		print(' '*(6-i-1)+'*'+' '*i)

	# or
	 # i=1
	 # j=4
	  #for rows in range(6):
	  	#for col in range(6):
	  		#if rows==0 or rows==5:
	  			#print('*',end='')
	  		#elif rows==i and col==j:
	  		   # print('*')
	  		   # i+=1
	  		    #j-=1
	  		#else:
	  		    #print(end=' ')
	  	#print()	        	


#for rows in range(6):
    #for col in range(6):
        #if rows+col==5 or rows==0 or rows==5:
            #print('*',end='')
       # else:
       #     print(end=' ')
    #print()       
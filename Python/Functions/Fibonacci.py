def fib(n):
    a=0
    b=1

    if n==1:
        print(a)
    elif n<=0:
        print ("The Number must be a positive ")

    else:
        print(a)
        print(b) 

    for i in range(2,n):
        
        
        c=a+b
        a=b
        b=c
        print(c)
               
fib(15)    




    




#def fib(n):
    #if n>=0: # NOt my code code was supposed to print sum less than 100
     #   a=0 
      # b=1 
       # print(a) 
        #print(b) 
    #else: 
     #   print("should not be negtive number")
    #for i in range(2,n): 
     #   c=a+b 
      #  a=b 
       # b=c  
    #if c<100:
     #   print(c) 

#fib(15 )



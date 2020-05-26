#factorial
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
result=fact(5)        
print(result)        



#Recursion



def fac(n):
    if n==0:
        return 1

    return  n * fact(n-1)#------> function calling itself like 5*4! then 4*3! and so on
result=fact(5)   
print(result) 





   







    

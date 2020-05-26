pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1    
         
    return False
list=[2,5,6,9,10,11]  
n=9 
if search(list,n):
    print('Found at',pos)

else:
    print('Not found')           
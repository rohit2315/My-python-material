a=10 # global variable

def some():
    a=15               # local 
    print('in',a)
some()    

print('out',a)






def somen():
                
    print('in',a)# accessing global in local
somen()    

print('out',a)









def somes():
    global a   # by using global i changed the global var
    a=15               # local 
    print('in',a)
somes()    

print('out',a)





def something():
    global a               # local 
    print('in',a)
    a=9             #------> here it will treat 9 as global and not as local so see next
something()    

print('out',a)
 


a=10
print(id(a))
def someone():
    a=9

    x=globals()['a']# first access then changed below
    print(id(x))#------>access the global var address
    print('in',a)
    globals()['a']=15 # Hence we can change the global variable without affecting local
someone()
print('out',a)    

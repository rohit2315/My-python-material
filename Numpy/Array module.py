from array import *#* means all the function from array module

var=array('i',[1,-2,3,4])
print (var)
print(var.buffer_info())
#array('i', [1, 2, 3, 4])
#(2268619305072, 4)------> memory location and size


var=array('I', [1, 2, 3, 4])
print (var)
print(var.buffer_info())

var=array('i',[1,-2,3,4])#-----> similarly for char use "c" see other type also
for a in var:# for i in range(4)orrange(len(var))
    print(a)


var=array('i',[1,-2,3,4])   
newarray=array(var.typecode,[a for a in var]) 
for a in newarray:#i=0 while i<len(newarray): print(newarray[i]) i+=1
    print(a)



# Value from the user

val=array('i',[])
n=int(input("Enter the num:"))  
for i in range(n):
    x=int(input('Enter the value:'))
    val.append(x)
print(val)    


#Index of an array value

val=array('i',[])
n=int(input("Enter the num:"))  
for i in range(n):
    x=int(input('Enter the value:'))
    val.append(x)
print(val) 

a=int(input("Enter the value for search"))
k=0
for e in val:
    if e==a:
        print(k)
        break
    k+=1
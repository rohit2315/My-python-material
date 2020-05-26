import numpy as np
#Indexing
a=np.array([1,2,3])
print(a[1])

a=np.array([[1,2,3],[4,5,6]])
print(a[1][2])#a[i][j]


a=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(a)
print(a[0][1][2])#-----> see amulys indexing lec for 3 dimensional array a[i][j][k]
#[i=no of 2d array][j=no of rows][k=no of columns] ex 0 means 2d array in that j=1 that is 2 row and 3 coloumn

#Slicing
a=np.array([1,2,3,4,5,6,7])
print(a[1:])
print(a[2:5])
print(a[::2])#a[start:end:step]


a=np.array([[1,2,3],[4,5,6]])
print(a[1:,2:])#a[start:end:step,start:end:step]
print(a[:,1:])
print(a[:1,2:])




a=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(a)
print(a[:1,:1,1:2])#a[start:end:step,start:end:step,start:end:step]
print(a[::,::2,::2])
print(a[::,::,:1])


#Advanced indexing
a=np.arange(1,10)
print(a)
index=np.array([1,4,5])#---> first method storing index position values in a diff var 
print(a[index])

     #or
print(a[[1,4,5]])#-----> Directly using the index position



a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[[0,2],[2,0]])#----> to access 3&7 row=0&2 and column=2&0
print(a[[0,2],[2,0]])#----> to access 1&9 row=0&2 and column=0&2
print(a[[0,1,2],[1,1,1]])



a=np.arange(1,10)
print(a)
print(a[[2,5,2,5,2,5]])#----> to access the same element repeatedtly

#Boolean indexing

a=np.array([1,2,-2,-5,6,7])
print(a[a<0])

a=np.array([[1,-2,-3],[5,6,-7]])
print(a[a>0])

#Arithmetic operator
a=np.arange(1,5)
b=np.array([10,11,12,13])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#----------------x-----------------x-----------------x--------------------x-------------------x----------------------

sum=0
for i in range(1,10):
   
    if i%3==0 or i%5==0:
        sum+=i 
print(sum) 


lst=[0,1]
for i in range(0,10):
    add=lst[i]+lst[i+1]
    lst.append(add)
print(lst)

x,y=0,1
add=0
n=int(input("Enter a positive number:"))
while add<n:
    print(x)
    add=x+y
    x=y
    y=add
    add+=1

    


     
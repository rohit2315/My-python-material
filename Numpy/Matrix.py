import numpy as np
a=np.array([[10,20],[30,40]])
b=np.array([[1,2],[3,4]])
print(a*b)
print(a.dot (b))# matrix like multiplication (in array we use dot method)
#help(np.dot)
#Matrrix is class in numpy  numpy.matrix(data,dtype=none,copy=true) data=string or aray like object2
# matrix are always 2d 
# can use * for multiplication
a1=np.matrix("1 2;3 4")
print (a1)
b1=np.matrix([[10,20],[30,40]])
print(b1)
print(a1*b1) #here in matrix class we can use the astrik symbol
print(b1.T)

                          #Inverse 
c=np.array([[1,2],[3,4]])  # only square matrix can be inversed
d=np.linalg.inv(c)   
print(d) 
# for checking   
print(c.dot(d))
print(np.allclose(np.dot(c,d),np.eye(2)))  # this method also for checking

e=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(np.linalg.inv(e))
# in case of 3darray it will get inverse of 2 2d array see help

                       #Power numpy.linalg.matrix_power(a,n)
print(np.linalg.matrix_power(b,2))                       
print(np.linalg.matrix_power(b,3)) 
print(np.linalg.matrix_power(b,0)) # will give identity matrix
print(np.linalg.matrix_power(b,-2)) # first it will found out the inverse and then square  see below 
b2=np.linalg.inv(b)
print(np.linalg.matrix_power(b2,2))

                          #Linear Equation numpy.linalg.solve(a,b)#Ax=B A&B are square matrix
                          #3x+y=9 x+2y=8
x=np.array([[3,1],[1,2]])
y=np.array([9,8])
print(np.linalg.solve(x,y))
#6x+2y-5z=13,3x+3y-2z=13,7x+5y-3z=26
r=np.array([[6,2,-5],[3,3,-2],[7,5,-3]])
s=np.array([13,13,26])
print(np.linalg.solve(r,s))

                   #Determinant numpy.linalg.det(a)
print(np.linalg.det(a))                   
print(np.linalg.det(b)) 
print(round(np.linalg.det(b)))
print(np.linalg.det(r))

import numpy as np


#Attributes of Array
#Dimension
a=np.array([1,2,3])
print(a.ndim)
#1-----> Rank of an array 


a=np.array([[1,2,3],[3,5,6]])
print(a.ndim)
#2----->Rank of an array 

#Shape
a=np.array([1,2,3])
print(a.shape)
#(3,)----> 	Tuple of array dimensions

a=np.array([[1,2,3],[3,5,6]])
print(a.shape)
#(2, 3)----> 2 rows and 3 columns--->	Tuple of array dimensions


#Size
a=np.array([1,2,3])
print(a.size)
#3----> No of elements

a=np.array([[1,2,3],[3,5,6]])
print(a.size)
#6 -----> No of elements

c=np.zeros((2,3,4))
print(c.shape)
#(2, 3, 4)
c=np.zeros((2,3,4))
print(c.size)
#24----> 2*3*4=24

#Dtype
c=np.zeros((2,3,4))
print(c.dtype)
#float64

a=np.array([[1,2,3],[3,5,6]])
print(a.dtype)
#int32

#Item Size
a=np.array([[1,2,3],[3,5,6]])
print(a.itemsize)
#4---->32/8=4 byte


c=np.zeros((2,3,4))
print(c.itemsize)
#8---->64/8=8 byte

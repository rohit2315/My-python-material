import numpy as np

#Rules
#1. Size of each dimension should be same
#2. Size of one of the dimension should be 1


#Rule 1:if  the two arrays differ in their number of dimension,the shape of the one  fewer dimension is padded with ones on its leading side(left side)
#Rule2:If the shape of the two arrays does not match in any dimension, the array with shape equal to one  in that dimension is stretched to match the other shape.
#Rule3:If in any dimension the sizes disagree and neither equal to 1,an error is raised.

a=np.array([[1,2],[3,4],[5,6]])
b=np.array([1,2,3])
c=np.array([10,20])
print(a.shape)#(3,2)
print(c.shape)#(1,2)Rule1  #(,2 )same size and (1,) one of is satisfy
print(a+c)

d=np.array([[1],[2],[3]])
print(d.shape)
e=np.array([1,2,3])
print(e.shape)
print(d+e)
     #Summary Note:broadcasting not for scalars
     #1 shape of array 
     # 2. check the dimension 
     # 3.check size of dimension

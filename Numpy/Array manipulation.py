import numpy as np 
                                         #Reshape 
                                         #syntax
#numpy.reshape(array.shape,order)order=('C-rowwise opr,F-coloumnwise opr,A-fortan like memory opr')default=c
#arrayname.reshape(shape,order)
a=np.arange(10)
print(a)
b=np.reshape(a,(5,2))
print(b)
c=np.reshape(a,(5,2),order="F")
print(c)
#d=np.reshape(a,(4,2))
#print(d)
#Here the  size of d is 8 and a is 10 so no of elements not same there will be an error
                                       #RESIZE
e=np.arange(5)
print(np.resize(e,(3,2)))#np.resize doesnt change original array
e.resize((5,2))  # changes original array
print(e)                     






                                    #Flatten
f=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])#3D
print(f.flatten())
print(f.flatten(order='F'))

g=np.array([[1,1,3],[5,6,7]])  
print(g.flatten())                                  
                                   
                                   #Ravel 
                                   #syntax numpy.ravel(a,order="") or ndarray.ravel(order='')
print(np.ravel(f))
print(np.ravel(g,order='F'))                                   








                                             #Transpose() syntax numpy.transpose(array,axes=none) 
                                             # or ndarray.transpose(axes)

array1=np.arange(1,11).reshape(5,2)#default
print(array1)
print(array1.shape)
print(np.transpose(array1)) 
print(np.transpose(array1).shape)                                           



array2=np.arange(1,25).reshape(2,3,4)# axis0=2,axis1=3,axis2=4
print(array2)
print(np.transpose(array2))
print(np.transpose(array2).shape)
print(np.transpose(array2,(1,2,0)))#3-2darray,4-rows,2-coloumns





                                        #Swapaxes()
                                        #numpy.swapaxes(array,axis1,axis2)

print(np.swapaxes(array1,0,1))
print(np.swapaxes(array2,1,2))

print(np.swapaxes(array1,0,1).shape)
print(np.swapaxes(array2,1,2).shape)




                                       #Concatenate 
                                       # syntax:numpy.concatenate(arrays,axis=0,out=none) axis default 0 
a1=np.arange(1,5)
b1=np.arange(6) 
print(np.concatenate((a1,b1))) 
c1=np.zeros(10)
print(c1)
#print(np.concatenate((a,b),out=c1))    Error even though no elements in c is 10 that is (a1+b1) out is to store result of ab in c 
#print(c)


a2=np.array([[1,2],[3,4]])#(2,2)
b2=np.array([[5,6]])#(1,2)
print(np.concatenate((a2,b2)))#axis=0 it means we will join rowwise as (,2)=(,2) other dimension should be same like 2 opp row
#print(np.concatenate((a2,b2),axis=1))  #(2,)=!(1,) bcoz for joining column wise 2=!1 that is check other axis opp to axis which need to be added

print(np.concatenate((a2,b2.T),axis=1))#t=transpose (2,2) and (2,1)






                                         #Vstack():numpy.vstach(tuple) v-vertically join
                                      #                    |
                                         #              concaatenate(axis=0)

a3=np.arange(6)
n=np.arange(5)
c3=np.arange(5)
print(np.vstack((c3,n)))
#print(np.vstack((a3,n)))(1,6)&(1,5) axis=0 opp coloumn doesnt match
#vstack behaves different in 1d array  and we will get 2d array but same as concatenate in 2d 3d  with axis=0

                                    #hstack() numpy.hstack(tuple) h-horizontal axis=0--->1d & 2d,3d,4d same as concatenate with axis=1

print(np.hstack((a3,n)))


                                    #Spliting numpy.split(array,section,axis=0)

f=np.arange(1,10)# strange element is taking from 0
print(np.split(a,2))

e=np.arange(1,13).reshape(6,2)
print(np.split(e,2))


              #numpy.hsplit(array,section,axis=1)
              #numpy.vsplit(array,section,axis=0)





                                     #Insert numpy.insert(array,obj,values,axis=none) obj=index 
print(np.insert(f,1,50)) # 50 is inserted betn index1 and 2
print(np.insert(f,(1,4),50)) # 50 is inserted betn index1 and 2 and index 4&5
print(np.insert(a2,1,23))#flatten if axis not mention for 2d
print(np.insert(a2,1,23,axis=0))
print(np.insert(a2,1,23,axis=1))
print(np.insert(a2,1,[1,2],axis=0))
#print(np.insert(a2,1,[1,2,3],axis=0)) error we have 3 elements cant add

                                    #Append() numpy.append(array,values,axis=none)
print(np.append(a2,23))
print(np.append(a2,[[4,5]],axis=0))
#print(np.append(a2,[[4,5]],axis=1))
print(np.append(a2,[[4],[5]],axis=1))

                                     #Delete numpy.delete(array,obj,axis=none)
print(np.delete(f,2))  
print(np.delete(a2,1,axis=0))# here axis is 0,1 if u will take obj=2 error  
print(np.delete(a2,1,axis=1))                               
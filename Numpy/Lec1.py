import numpy as np #shortform of numpy
a=np.array([3,6,9,12])
print(a/3)
#[1. 2. 3. 4.]

                        #  Numpy Array functions


#help(np.array)
#Help on built-in function array in module numpy:

#array(...)
  #  array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)


# EXAMPLES
  
  
np.array([1,2,3])
    # >>> np.array([1, 2, 3], ndmin=2)
    #array([[1, 2, 3]])

  #upcasting
print(np.array([1,2,3.0])) #Here the data type is upcasted to float   
#[1. 2. 3.]

#More than one dimesnsion 
print(np.array([[1,2],[3,4]]))
#[[1 2]
# [3 4]]

#Type Provided 
print(np.array([1,2],dtype=complex))
#[1.+0.j 2.+0.j]

#Array also by tuple
print(np.array((1,2,3)))

     #Arange fun
#help(np.arange)
    #arange([start,] stop[, step,], dtype=None)
print(np.arange(1,10))
#1 2 3 4 5 6 7 8 9]
#np.arange(3) # start is optional
# array([0, 1, 2])

print(np.arange(1,10,2))
#1 3 5 7 9]

print(np.arange(1,10,2,dtype=complex))
#[1.+0.j 3.+0.j 5.+0.j 7.+0.j 9.+0.j]


#Zeros fun

#help(np.zeros)
# zeros(shape, dtype=float, order='C')#order is how to store in memory 
print(np.zeros(3))
#[0. 0. 0.]

print(np.zeros((3,2),dtype=int))
#[[0 0]
# [0 0] 
# [0 0]]



b = np.zeros((3), dtype=[('x', float), ('y', int)]) 
print(b) 
#[(0., 0) (0., 0) (0., 0)]

#Ones fun
help(np.ones)
#ones(shape, dtype=None, order='C')

print(np.ones(5))
#[1. 1. 1. 1. 1.]
print(np.ones((5),dtype=int))
#[1 1 1 1 1]

#similarly empty

print(np.empty((3,4),dtype=int))
#[[ 510853120          0  134350337  302059009]
 #[ 234949121  167906305  234948609  201395713]
 #[ 201395714 1310489089 1415934831 1702130533]]

 #Linspace
help(np.linspace)#-----> evenly spaced like arange but diff parameters
#linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

print(np.linspace(1,100,num=5))
print(np.linspace(2,3,num=5))
#[  1.    25.75  50.5   75.25 100.]----> Here 5 num  is evenly spaced betn 1&100
# [2.   2.25 2.5  2.75 3.  ]

print(np.linspace(1,100,num=5,endpoint=False))
#[ 1.  20.8 40.6 60.4 80.2]---> excluding last num

print(np.linspace(1,100,num=4,retstep=True))
#(array([  1.,  34.,  67., 100.]), 33.0)---> shows the diff betn each num(33)

print(np.linspace(1,100,dtype=int))
#[  1   3   5   7   9  11  13  15  17  19  21  23  25  27  29  31  33  35
#  37  39  41  43  45  47  49  51  53  55  57  59  61  63  65  67  69  71
 # 73  75  77  79  81  83  85  87  89  91  93  95  97 100]--> By def num=50


 #Eye and Identity 

help(np.eye)
#eye(N, M=None, k=0, dtype=<class 'float'>, order='C')
# Return a 2-D array with ones on the diagonal and zeros elsewhere.

print(np.eye(3))
#[[1. 0. 0.]
# [0. 1. 0.]
#[0. 0. 1.]]
print(np.eye(3,2))
#[[1. 0.]
 #[0. 1.]
 #[0. 0.]]---> Here the coloumn is optional by default=row
print(np.eye(3,k=1))
#[[0. 1. 0.]
#[0. 0. 1.]
#[0. 0. 0.]]---> shifts one above main diag
print(np.eye(4,k=-2))
#[[0. 0. 0. 0.]
 #[0. 0. 0. 0.]
 #[1. 0. 0. 0.]
 #[0. 1. 0. 0.]]---> shifts 2 down main diag

# identity sq matrix
print(np.identity(3,dtype=int))
#[[1 0 0]
 #[0 1 0]
 #[0 0 1]]

 #Random Module
print(np.random.rand(2,3))
#[[0.60389175 0.08182575 0.72583395]
 #[0.63301249 0.08629567 0.53681297]]

print(np.random.randn(2,3))
#[[ 1.42812969  1.074644    1.01916419]
# [-1.03226334  0.62121491  0.02038218]]

print(np.random.ranf(5))
#[0.40579579 0.89884267 0.19563271 0.63591283 0.11719001]
print(np.random.randint(5,size=5))
#[4 1 4 0 1]
print(np.random.randint(5,size=(2,4)))
#[[3 1 0 2]
# [3 1 3 0]]----> nums betn 0 to 4 with matrix 2x4--->see parameters using help of all

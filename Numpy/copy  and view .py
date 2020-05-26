
from numpy import *


arr1=([1,2,3,4,5,6])
print(arr1)

arr2=arr1#-----> by normal copying we will get same memory location
print(arr2)
print(id(arr1))
print(id(arr2))
#2086807692744
#2086807692744-----> both array have same address 


arr1=array([1,2,3,4,5,6])
arr2=arr1.view()#-----> Here view function will create 2 diff array at diff adress
print(arr1)
print(id(arr1))
print(id(arr2))
#1615538306544
#615538306384

arr1=array([1,2,3,4,5,6])#Shallow copy changes indx in arr1 and 2 both
arr2=arr1.view()#-----> Here view function will create 2 diff array at diff adress
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
#[1 7 3 4 5 6]
#[1 7 3 4 5 6]
#1930752413088
#1930752413248

arr1=array([1,2,3,4,5,6])#Deep copy changes indx in arr1 only
arr2=arr1.copy()#-----> Here copy function will create 2 diff array at diff adress
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
#[1 7 3 4 5 6]
#[1 2 3 4 5 6]
#2503647444464
#2503645626000







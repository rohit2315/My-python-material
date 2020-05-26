#Lambda functions are basically a fun which u need to use once or two in your code 
f=lambda a: a*a
result=f(5)
print(result)


f=lambda a,b: a+b
result=f(5,6)
print(result)




#Use of lambda in filter map and reduce 
#help(filter)
#help(map)
#help(reduce)
from functools import reduce
num=[2,4,3,5,8,9,10,12]
evens=list(filter(lambda n:n%2==0,num))#filter(fun,sequence or list on which to be performed)
doubles=list(map(lambda n: n*2,evens))#map applies the operation on a data
sum=reduce(lambda a,b: a+b,doubles)
print(evens)
print(doubles)
print(sum)
#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

#Working : 

#At first step, first two elements of sequence are picked and the result is obtained.
#Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
#This process continues till no more elements are left in the container.
#The final returned result is returned and printed on console.


#filter() in python The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. syntax: filter(function, sequence) Parameters: function: function that tests if each element of a sequence true or not.


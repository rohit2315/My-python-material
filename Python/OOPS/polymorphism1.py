        #operator overloading  whenever we are calling a operator it calls a method behind the scene int knows '+' str knows'+'
        #class doesnt know

        #operator                methods
        #add                  __add__(self,other)
        #sub                  __sub__(self,other) 
        #multi                __mul__(self,other)
        #so on 
        #

#class student:

    #def __init__(self,m1,m2):

        ##self.m1=m1
       # self.m2=m2

#s1=student(10,20)
#s2=student(30,40)
#s3=s1+s2            #student class cant understand this operand so we have to overload the method ,so we need to define
#                    the method which happens behind the scene so that our class can understand
           


class student:

    def __init__(self,m1,m2):

        self.m1=m1
        self.m2=m2

    def __add__(self,other):  #self=s1 other=s2
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self,other):
        x=self.m1+self.m2
        y=other.m1+other.m2
        if x>y:
            return True
        else:
            return False


    def __str__(self):
        #return self.m1,self.m2  --> for this print(s1.__str__()) will give result in tuple
        return('{} {}'.format(self.m1,self.m2))          


s1=student(60,20)
s2=student(30,40)
s3=s1+s2           #--->student.__add__(s1,s2) 
print(s3.m1)
if s1>s2:
    print('s1 wins')
else:
    print('s2 wins') 

a=9
print(a)
#print(s1.__str__())     #behind the scene its calling str method and prints addressif _str__not defined whereas it str or int object 
             # student is not defined so we need to def str method for s1 obj  to print its value
print(s1)

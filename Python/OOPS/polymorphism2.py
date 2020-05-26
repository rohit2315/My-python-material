 #method overloading
# we cant write 2 same methods like sum in one(a,b) and other (a,b,c) so we have to use logic or condition 
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else :
            return a 
             

s1=student(6,5)
print(s1.sum(5,5,7))




                  #Method overriding


class A:
    def show(self):
        print('im in A')


class B:
    pass

m=A()
m.show()



class A:
    def show(self):
        print('im in A')


class B(A):# here i am accessing  A as inheritance bcoz b has no attr show
    pass

m=B() 
m.show()




class A:
    def show(self):
        print('im in A')


class B(A):# here b has show fun so it will overwrite the inheritance and will print b 
    def show(self):
        print('im in b')
    

m=B() 
m.show()




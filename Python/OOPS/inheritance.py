
#multilevel inheritance
class A:
    def feature1():
        print('feature 1 working')

    def feature2():
        print('feature 2 working') 

class B(A):            #B can access A
    def feature3():
        print('feature 3 working')
    def feature4():
        print('feature 4 working')
    





class C(B):         #c can access a and b
    def feature5():
        print('feature 5 working')

        



a=C()



        

#multiple inheritance
class A:
    def feature1():
        print('feature 1 working')

    def feature2():
        print('feature 2 working') 

class B():            
    def feature3():
        print('feature 3 working')
    def feature4():
        print('feature 4 working')
    





class C(A,B):         #c can access a and b
    def feature5():
        print('feature 5 working')

d=C()








                       # constructor in inheritance


class A:
    def __init__(self):    #constructor A will call it automatically
        print('in init a')  

    def feature():
        print('feature 1 working ') 


class B(A):
    def feature():
        print('feature 2 working')



a=A()        


      











class A:
    def __init__(self):    #constructor A will call it automatically
        print('in init a')  

    def feature():
        print('feature 1 working ') 


class B(A):
    def __init__(self):
        super().__init__()
        print('in init b')

    def feature():
        
        print('feature 2 working')


a=B()        # it will call its init only and not a's even though we are inheriting to acces init of a we use super method
  # when u create object of subclass it will call init of subclass 
  # when you call super it will call init of super class first and then init of subclass








    
class A:
    def __init__(self):    #constructor A will call it automatically
        print('in init a')  

    def feature():
        print('feature 1 working ') 


class B():
    def __init__(self):
        
        print('in init b')

    def feature():
        
        print('feature 2 working')


class C(A,B):
    def __init__(self):
        super().__init__()
        print('in init c')

    def feature3():
        
        print('feature 3working')        


a=C() 
#method resolution order(MOR) it means it will always go from left to right therefore it prints init of a and c and not b       








    

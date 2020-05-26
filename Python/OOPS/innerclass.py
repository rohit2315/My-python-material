class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno


    def show(self):
        print(self.name,self.rollno)
     
            

s2=student('Rohit',2)
s2.show()


#-----------------------------x==========x------------------x-xxxxxxxxxxxxxxxxxxxx

class students:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        


    class laptop :                  
        def __init__(self) :
            self.brand='DELL'
            self.ram=8
            self.cpu='i5' 

        def shows(self):
            print(self.brand,self.ram,self.cpu)
    
s3=students('Rahul',1)
print(s3.name,s3.rollno)
lap1=students.laptop()
# creating inner class object outside of outer class then to access inner class mention outer class last line see




#------------------------x--------------------------------x-------------------------x-----------------x-----------

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

# creating inner class object inside outer class we use above method
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop :

        def __init__(self) :
            self.brand='DELL'
            self.ram=8
            self.cpu='i5' 

        def show(self):
            print(self.brand,self.ram,self.cpu)    
     
            

s2=student('Rohit',2)
s2.show()






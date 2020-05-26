class computer:
    def __init__(self):
        self.name='rahul'
        self.age=12

    def update(self) :
        self.age=30

    def compare(self,other) :#compare(whose calling it,whom to compare)
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c1.age=32
c2=computer() 
if c1.compare(c2):#c1=self and c2=other we can do reverse
    print('They are same')  
else:
    print('They are not same')    

c1.update()
print(c1.age)
                


# here self is c1& other is c2 
# if there are 10 objects and we need to call a object self does that work at that instance 
#diff obj has diff memory called heap memory and constructor decides in classs 
# size of an object depends upon no variables it has 
# constructor(computer())here allocates the size
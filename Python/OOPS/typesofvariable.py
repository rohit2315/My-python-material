class car:
    Wheels=5  #class(static) variable is same for all object
    def __init__(self):
        self.mil=10   #----> they are instance variale it means they can change for diff  object
        self.com='BMW'

c1=car()
c2=car() 
c1.mil=8
car.Wheels=6       
print(c1.mil,c1.com,c1.Wheels)
print(c2.mil,c2.com,c2.Wheels)

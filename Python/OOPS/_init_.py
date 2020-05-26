class computer:
    def __init__(self,cpu,ram):# init method is builtin and it takes arguent=variable to instantiate object
        self.cpu=cpu #self is an object here
        self.ram=ram

    def config(self) :
        print('config is',self.cpu,self.ram)
        
    def update(self) :
        self.age=30    

comp1=computer('i5',16)
comp1.config()
comp1.update()
       



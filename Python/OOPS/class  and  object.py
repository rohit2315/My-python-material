#in python everything is object inbuilt class is str,int
# attributes=variable , behaviour=methods(function) 
# in class function is called methods



class computer:
    def config(self):
        print('i5','16gb')

comp1=computer()        # comp1=object
computer.config(comp1) # class.method(object)---->calling method

comp1.config()   # object.method()--->another calling method


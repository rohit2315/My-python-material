class student:
    school='Rahul'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self) :# instance method is used to work on objects self
        return (self.m1+self.m2+self.m3)/3  

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():# we dont pass anything
        print('this is static method')



s1=student(23,31,21)    
s2=student(35,38,45) 
print(s1.avg())
print(student.getschool())
student.info()
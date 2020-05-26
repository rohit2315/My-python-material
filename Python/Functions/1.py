def greet():    #------> function
    print("Hello")
    print("Good Morning")
greet()    #-----> calling a function

def add(x,y):#x&y are arguments
    print(x+y)
add(4,5)  



def add_(x,y):# Here the function is returning a value and it has done its work and stored in result so by printing it i will display the result.
    c=x+y    # if u wont write print it will not display the result
    return c
result=add_(4,5)
print(result)


def add_sub(x,y):#one function multiple values 
    c=x+y
    d=x-y
    return c,d  # returning 2 values 
result1,result2=add_sub(4,5) # Here accepting 2 values
print(result,result2)


#pass by value =passing a value not the addr to a fun or another var which is stored in diff memory
#pass by reference=passing the add along with value having same memory
#In python we dont have any of it******* because int and strings are immutable
#Telusko lec 33
def update_(x):#---> passing 10 but then changed to 8
    print(id(x))
    x=8
    print(x)
    print(id(x))
a=10
update_(10)
print(a)
print(id(a))  
#140715401781936-->same
#8
#140715401781872--->updated
#10
#140715401781936 --->same 


def updates(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print('x',lst)

lst=[10,20,30]
print(id(lst))
updates(lst)
print(lst)    

#2134619083208  ------>list are mutable as they have same adress hence its upating the original also
#2134619083208
#2134619083208
#x [10, 25, 30]
#[10, 25, 30]


#Types of arguments
def sum(a,b):#-->formal argument
    c=a+b
    print(c)
sum(6,5)  #--->actual argument  


def person(name,age):
    print(name)
    print(age)  
person('Navin',28)# position argument
person(28,'Navin')


def persons(name,age):
    print(name)
    print(age)  
persons(age=28,name='Navin')#-----> keyworded argument


def pers(name,age=18):
    print(name)
    print(age)  
pers('Navin') #----> Default


def  sums(a,*b):# here a is assigned 5 and b is a tuple and we cant add int and tuple so loop
    c=a              #or sums(*a) c=0 same
    for i in b:
        c+=i
    print(c)
sums(5,10,20,30)    #varaiable length argument 

def per(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
per('Rahul',age=26,city='Mumbai',Mob_No=8698324853)  #Kwargs keyworded variable length argument  


# Pass List to functions

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[2,3,4,5,6,7,8,12,15,19]
even,odd=count(lst)
print('Even:{} and Odd:{}'.format(even,odd))   



def counts(a):


    for i in a :
        if len(i)>=5:
            print(i)
        else:
            print('{} length is less than five'.format(i))
counts(a=['Rahul','Sujay','Manish','Sumeet','Manoj','Ashu'])









import sys
sys.setrecursionlimit(2000)   # greet will not execute infinite times so if u want to run the code to a limit use this 
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print('Hello World',i)
    greet()
greet()    


#multithreading: when we run a multiple application on a device they use all thr cores to function properly
#Ex: in car race game we have you,enemy,police they all are individual threads of a game and need to work simultaneously 
# this is the concept of thread we need somethhing to execute properly at the same time

from time import sleep
from threading import *

class Hello(Thread): #Thread is main thread  and run function is compulsory in thread and not other name see thread fun 
    def run(self):
        for a in range(5):
            print("Hello")
            sleep(1)
# sleep is used so that hello hi dont coincide at same time so a gap of 1 sec 
        
        
class Hi(Thread):
    def run(self):
        for i in range(5):
           print('Hi')
           sleep(1)

t1=Hello()
t2=Hi() 
t1.start()
 # we dont write fun name we write start see thread fun bcoz if we write run then it will print all 
#hello first and then hii as singles threa

sleep(0.2)# we want gap so that hello hii dont coincide
t2.start()

t1.join()
t2.join()
#we use join fun bcoz here we are telling main thread fun to let join t1 and t2 thread first and then print 
#bye since main thread is idle it will print bye in between 

print('Bye')


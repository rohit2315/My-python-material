#polymorphism-many forms of object


#x=7
#x='string    x is just the name if we check type of x it will show type of int and str

                 #Duck Typing

class pycharm:
    def execute(self):
        print('compiling')
        print('running')

class laptop:
    def code(self,ide):
        ide.execute()     

ide=pycharm()
lap1=laptop()
lap1.code(ide)                





class pycharm:
    def execute(self):
        print('compiling')
        print('running')


class vscode:
    def execute(self):
        print('spell check')
        print('compiling')
        print('running')


class laptop:
    def code(self,ide): # ide is not fixed for pycharm its a dynamic  typing so no matter which cls it should have object execute  
        ide.execute()     

ide=vscode()
lap1=laptop()
lap1.code(ide)                
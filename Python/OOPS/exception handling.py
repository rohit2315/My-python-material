a=5
b=2
try:
    print('case opened')
    print(a/b)
    k=int(input('Enter the num:'))
    


except ZeroDivisionError as e:
    print('You cannot divide a num by zero')

except ValueError:
    print('you have an invalid input ')

except Exception as e:
    print('something went wrong')    

finally:
    print('case closed')    

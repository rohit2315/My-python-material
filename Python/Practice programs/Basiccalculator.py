num1=float(input('Enter the num:'))
operator=input('Enter the operator:')
num2=float(input('Enter the num:'))
if operator=='+':
	print(num1+num2)
elif operator=='-':
	print(num1-num2)
elif operator=='*':
	print(num1*num2)
elif operator=='/':
    print(num1/num2)
else:
    print('Invalid Operator')    	


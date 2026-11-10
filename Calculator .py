num1= float(input('please enter the frist number : '))

operator = input('please enter the operator : ')

num2 = float(input('please enter the second number : '))

if operator == '+' :
	print (num1+num2)
	
elif operator == '-' :
	print (num1 - num2)

elif operator == '*' :
	print (num1*num2)

elif operator == '/' :
	print (num1/num2)

else :
	print('Wrong Operator please try again')
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "cannot divide by zero!"

while True:
    try:
        num1 = float(input('please enter the first number : '))
        operator = input('please enter the operator : ')
        
        if operator == "exit":
            print("شكراً لاستخدام الآلة الحاسبة!")
            break
            
        num2 = float(input('please enter the second number : '))
        
        if operator == '+':
            print("Result:", add(num1, num2))
            
        elif operator == '-':
            print("Result:", subtract(num1, num2))
        
        elif operator == '*':
            print("Result:", multiply(num1, num2))
        
        elif operator == '/':
            print("Result:", divide(num1, num2))
        
        else:
            print('Wrong Operator please try again')
            
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

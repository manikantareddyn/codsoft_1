# code for simple calculator
# defining all arithmetic operations
def add(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def modulo_division(x,y):
    return x%y
import math
def squareroot(x):
    return math.sqrt(x)
def factorial(x):
    return math.factorial(x)
print('CHOICES : ')
choice=int(input(print("""
Enter 1 for Addition
Enter 2 for subtraction
Enter 3 for Multiplication
Enter 4 for Division
Enter 5 for modulo division
Enter 6 for finding sqare root of number
and Enter 7 for factorial of a number""")))
if choice==(6 or 7):
     num3=float(input('Enter a number :'))
else:
     num1=float(input('Enter 1st number :'))
     num2=float(input('Enter 2nd number :'))
if choice ==1:
      print(add(num1,num2))
elif choice ==2:
       print(subtraction(num1,num2))
elif choice ==3:
      print(multiplication(num1,num2))
elif choice ==4:
       print(division(num1,num2))
elif choice ==5:
      print(modulo_division(num1,num2))
elif choice==6 :
       print(squareroot(num3))
elif choice==7:
       print(factorial(int(num3)))
else:
       print('Invalid input')

                   
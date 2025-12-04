# Name= input("Enter Your Name:")

#print("My name is "+ Name)

'''
x= 23
 
y= str(x)

print(y)

num1= "100"

num2= int(num1)

print(num2)

print(type(num2))

num3=0.98

num4=int(num3)

num5=76
num6=float(num5)

print(num4,num6)

'''
'''

age=input("Enter Your Age:")

age=int(age)

if age>=18:
    print("Adults")

else:
    print("Not Adults")   

radius= input("Enter Radius:")

radius=int(radius)

area= 3.14 * radius * radius
print("Area of Circle is:", area)

'''
print("Enter a number:")
num=input()
num=float(num)
print(type(num))

if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

marks=input("enter your marks:")

marks=int(marks)

if marks>=75:
    print("A Pass")
elif marks>=65:
    print("B Pass") 
elif marks>=50:
    print("C Pass")
elif marks>=35:
    print("S pass")
else:
    print("Fail")    


number1=input("Enter first number:")
number2=input("Enter second number:")
number3=input("Enter third number:")  

number1=int(number1)
number2=int(number2)
number3=int(number3)

if (number1>number2) and (number1>number3) :
    print("Number 1 is highest number")
elif (number3>number2) and (number3>number1) :
    print("Number3 is highest number")    
elif (number2>number1) and (number2>number3) :
    print("Number2 is highest number")
    
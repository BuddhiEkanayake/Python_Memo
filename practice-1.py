# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

num1=input("enter number num1:")
num1=int(num1)

num2=input("enter number num2:")
num2=int(num2)

if (num1 * num2) > 1000 :
    print(num1+num2)
    
else:
    print(num1*num2)
# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

num1=input("enter number num1:")
num1=int(num1)

num2=input("enter number num2:")
num2=int(num2)

if (num1 * num2) > 1000 :
    print(num1+num2)
    
else:
    print(num1*num2)


#--------Second way of doing the same thing-----------------------------------------------------------


def produce(num1,num2) :
    product= num1*num2
    if product>1000:
        return num1+num2
    else:
        return product

print(produce(80,20))
name="John Smith"
age=20
print(name,age)

#--------------------------------------Variables----------------------------------------------------------------------------------------------

age=12
first_name="John"

#boolean values also we can store

print(first_name)

#-------------------------------------Receiving Input--------------------------------------------------------------------------------------------

name=input("What is your name? ")
print("Hello " + name)

#------------------------------------Type Conversions-------------------------------------------------------------------------------------------------

birth_year= input("What is your birth year? ")
age=2024-int(birth_year)

print( "my age is:" + str(age) )

First_number= input("first number: ")
Second_number= input("second number: ")

Sum= int(First_number) + float(Second_number)

print("SUM:"+ str(Sum))

#------------------------------------String-----------------------------------------------------------------------------------------------------


course= 'Python for Beginners'
print(course.lower())

print('y' in course) #true (we can get boolean values)

print('for' in course)#true (we can get boolean values)

print(course.find('for')) #7 (we can get index of the word)

print(course.replace('Beginners','Absolute Beginners')) #Python for Absolute Beginners

print(course.replace('for', '4')) #Python 4 Beginners

print(course[0:3])

#----------------------------------operators---------------------------------------------------------------------------------------

x=10

x+=7
print(x)

x-=7
print(x)

print(x/3)

print(x//3)

print(x**3)

x=4

print(x>3 or x>10)
print(x>2 and x<10)
print(not x>2)

#----------------------------------if/else-----------------------------------------------------------------------------------------------------------

temperature=input("What's the temperature like? ")
temperature=int(temperature)

if temperature>30:
    print("It's a hot day")
elif temperature>20: #temperature is greater than 20 and less than 30
    print("It's a nice day")
else:
    print("It's a cold day")

#-------------------------------------------------Exercise---------------------------------------------------------------------------------------------

    weight=input("Weight: ")
    weight=int(weight)

    answer=input("(K)g or (L)bs? ")
    if answer.upper()=='K':
        print(weight*0.45)
    elif answer.upper()=='L':
        print(weight/0.45)

    
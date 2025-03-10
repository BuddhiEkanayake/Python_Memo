for number in range(1,10,2):
    print("Attemt", number+1,(number+1)*".")

#--------If else with loop--------------------------------

successful = False

for number in range(3):
    print("Attemt")

    if successful:
        print("Successful")
        break
    
else:
        print("Not successful")


#-----------------Nested loops--------------------------------

for x in range(5):
     for y in range(3):
         print(f"({x},{y})")

#-----------------Iterables-----------------------------------

print(type(range(3)))

for x in "Python": #Iterate over a string
    print(x)

for x in [1,2,3,4]: #Iterate over a list
    print(x)

#-----------Exercise------------------------------------------
count=0

for x in range(1,10):
     if (x%2==0):
        count+=1   
        print(x)
print(f"We have {count} Even numbers.")        
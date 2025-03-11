def greet(first_name,last_name):
    print(f'Hi {first_name} {last_name}')
    print("wecome to the party")


greet("John","Cena") 

#function types-2
#1- perform a task
#2- return a value


def get_greet(name):
    return(f"hi {name}")

message= get_greet("Henry")
print(message)
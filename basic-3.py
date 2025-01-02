 
i = 0
while i<10:
    print(i)
    i=i+1 

while i<5:
    print('*' * i)

    i= i+1  
    print('Done')

  #-----------------------------------------lists----------------------------------------------------------------------------------------------------------

list = ['kamal', 'kumar', 'singh', 'lomba']
print(list)

print(list[0:3])

list[2]='Sajith'
print(list)

print(list[-2])

print(list[0:3:2]) #list[start:stop:step]

list.append('kumar')
print(list)

list.insert(2,'kumar')
print(list)

list.remove('kumar')
print(list)

print(len(list))

list.pop(2) #we can remove index
print(list)

list.clear()
print(list)

print('kamal' in list)





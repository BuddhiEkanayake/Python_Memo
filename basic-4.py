fruits = ['banana', 'apple', 'mango','orange']

for i in fruits:
    print(i)

numb = ['0','1','3','4']  
for i in numb:
    print(i)
    if i=='3':
        break

fruits = ['banana', 'apple', 'mango','orange']

for x in fruits:
    if x=='mango':
        continue
    print(x)
    

for x in range(6):
    print(x)

adj=['red','big', 'tasty']    
vrb=['apple','orange','banana']

for x in adj:
    for y in vrb:
        print(x,y)
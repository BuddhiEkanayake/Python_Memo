#while loop

i=0

while i<6 :

    print(i)
    i+=1

#for loop

for x in range(6):
    print(x)

#-----------------Practice Problems-----------------------------------    

#1.

for i in range(1,11):
    print(i)

#2.

for i in range(0,20,2):
    print(i)

x=0

while x<=20:
    print(x)
    x+=2

#3.
total=0
for i in range(0,100):
    tota = total+i
    print(total)    
#4.
name="hellow" 

for char in name:
    print(char)

#5.
i=0
j=input("Enter a Number:")
j=int(j)
total=0

for i in range(0,13):
    total=i * j
    print(j,"X",i,"=",total)

#6.
name="python loops"
vowels="aeiou"
count=0
for ch in name:
    if ch in vowels:
        count+=1
print(count)

#7.
name="buddhi"
name1=""
for ch in name:
    name1= ch+ name1


    
       
print(name1)


#8.
i=input("Enter your number")
i=int(i)

for j in range(1,100):
    if i%j==0:
        print(j)

#9.

for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i)  

#10.

for i in range(1,10):
    total=(i* '*')
    print(total)

#11.

list=[10,20,30,40]

for i in list:
    print(list.index(i),i)

#12.
i=1234
sum=0

for j in str(i):
    sum+=int(j)
print(sum) 


              
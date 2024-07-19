#Day1:Introduction to python
#Basic of python:Syntax,Variable,Data types

x=5
print(x)
5

#Integer

a=10
b=20
print(a)
10
print(b)
20
print(a+b)
30

#float

a=3.8
b=2.9
print(a)
3.8
print(b)
2.9
print(a+b)
6.699999999999999

#String

str1="Hai"
str2="Welcome to Kerala"
result=str1 +str2
print(result)

str="Data Analytics"
len=len(str)
print(len)
14

#Boolean

a=10
b=35
print(a==b)
False
c=10
print(a==c)
True
print(a!=b)
True
print(a>b)
False
print(a<b)
True
print(a>=b)
False
False
False

#if-else

x=30
if x>=18:
    print("you are adult")
else:
    print("you are not adult")


mark=100
if mark>=80:
    print("Grade:A")
elif mark>=70:
    print("Grade:B")
elif mark>=60:
    print("Grade:c")

#Loops(for,while)

for i in[1,2,3,4]:
    print(i)


a='hello'
for letter in a:
    print(a)

for i in range(10):
    if i%2 == 0:
        continue
    print(i)

for i in range(10):
    if i%2 == 0:
        break
    print(i)

#while loop

i=0
while i<5:
    print(i)
    i+=1

i=0
while i<5:
    print(i)
    i+=1
print("code is ended")

#sum numbers from 1 to 5
sum=0
number=1
while number <=5:
    sum +=number
    number +=1
print(sum)


# decimal to binary
num=int(input('enter no'))
binary=''
while num>0:
    rem=num%2
    binary=str(rem)+binary
    #print(rem)
    num=num//2
else:
    print(binary)

print(1%2)
# binary to decimal
import math
no=int(input('enter no'))
power=int(input('enter no'))
print(math.pow(no,power))
no=int(input('enter no'))
decimal=0
i=0
while no>0:
    rem=no%10
    value=rem*int(math.pow(2,i))
    decimal=decimal+value
    no=no//10
    i+=1
else:
    print(decimal)

# 3 table
start=1
while start<=100:
    if start%3==0:
        print(start)
    start+=1
#prime number
no=int(input('enter a number'))
div=2
while div<no:
    if no%div==0:
        print('not prime')
        break
        div+=1
else:
    print('prime')
# nestted loop
row=5
while row>=1:
    col = 1
    while col<=row:
        print('*', end=(' '))
        col+=1
    col2=5
    while col2>=row:
        print(row,end='')
        col2-=1
    print()
    row-=1
#string
s='python is very very easy'
position=-1
length=len(s)
print(length)
count=0
while True:
    position=s.find('y',position+1,length)
    if position==-1:
        break
    print(position)
    count+=1
# count using for
name='chabeer absal'
print(name.count('a',8,11))
name=name.replace('c','a')
print(id(name))
print(id(name))
print(name)
# string is immutable
s='python is very easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print(s[0:-1]+s[-1].upper())
mailid=input('enter your email id')
i=0
while i<len(mailid):
    if not mailid[i]>='0' and mailid[i]<='9':
        print(mailid[i],end='')
    i+=1
print()
for x in mailid:
    if not x>='a' and x<='z':
        if not mailid[i] >= '0' and mailid[i] <= '9':
            print(mailid[i], end='')
            print(x,end='')
        i+=1

a=[1,2,3,4,5,5,5,5,5]
print(len(a))
a.append(500)
print(a)
print(a.count(5))
count=0
while count<=len(a):
    if count==5:
        print(count)
    count+=1
print(a.index(4))
list=[]
for no in range(1,60):
    if no%2==0:
        list.append(no*no)
print(list)
l=[0,1,2,3,4,56,77,8]
l.insert(3,250)
l.insert(-1,2000)
print(l)
print(chr(65))
l1=['a','b','c']
print(id(l1))
l2=[1,2,3]
l1.extend(l2)
print(l1)
l1.extend('chabeer')
print(l1)
#functions
l=[10,20,30,40]
l.pop()
print(l)
print(id(l))
l3=[20,30,40,60]
print(id(l3))
l2=l.copy()
print(l2)
print(id(l2))
l.extend(l3)
print(l)
print(id(l))
l3.clear()
print(l3)
l.remove(20)
l.reverse()
print(l)
s1=input('enter first number')
s2=input('enter 2 number')
comb=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        comb=comb+s1[i]#chabeer
        i+=1
    if j<len(s2):
        comb=comb+s2[j]#absal
        j+=1
print(comb)
# input a5b6c7
#output abc567
i='a5b6c7'
o=''
p=''
for x in i:
    if x.isalpha():
        o=o+x
    else:
        p=p+x
o=o+p
print(o)
#tuble
t=(10,20,30,40,50,60,70,70,90)
print(t.count(60))
print(t[-1])
print(t[2:5])
print(t[::2])
t1=(20,50,70,90,100,45)
tt2=(964,86,879,00)
print(t1+tt2)
print(t1*0)
print(len(t))
print(t.index(30))
print(sorted(t,reverse=True))
print(min(t))
print(max(t))
print(sum(t))
a,b,c,d=10,20,30,40
t=a,b,c,d
print(t)
p,q,r,s=t
print(q)
a=(i**i for i in range(1,6))
for value in a:
    print(value,end=' ')
print()
print(type(a))
d=0
while d<4:
    t=eval(input('enter'))
    print(t)
    d+=1
# dictionary
d={}
d[123]='chabeer'
d[124]='absal'
print(d)
d1={1234:'chabeer',12345:'absal',12346:'absal',654:'aravinth',546:'harish'}
print(d1)
d1[345]='me'
print(d1)
del d1[345]
print(d1)
print(len(d1))
print(d1.get(1234))
print(d1.get(123456))
d1.pop(1234)

print(d1)
print(d1.popitem())
print(d1)

s={10,20,30,40,50}
e={20,30,40,60,70}
print(e)
print(s & e)
print(type(s))
s.add(35)
s.remove(20)
print(s)
a={}
print(type(a))
f=s.clear()
print(f)

print(tuple(e))
g=[10,20,30]
g[2]=37

print(g)
print(dir(e))
o={345,757,976}
#bublle sort
# [12345]=[15246784l
l=[1,0,5,6,3,8,6,9]
r=len(l)-1
for n in range(0,r):
    if l[n]>l[n+1]:
        result=l[n],l[n+1]=l[n+1],l[n]
        print(result)
def getusernamepassword(username,password):
    if username!='abcd':
        print('invalid username')
        username=input('enter username')
        password=input('enter password')
    elif password!='abcd':
        print('invalid password')
        username=input('enter username')
        password=input('enter password')
    else:
        print('correct')

username=input('enter username')
password=input('enter password')

getusernamepassword(username,password)
def display(n):
    print(n)
    n+=1
    if n<=5:
        display(n)
display(1)
z=4
x=5
y=5
def chabeer():
    global d
    d=5
    return x+y+z+d
ans=chabeer()
print(ans)
print(x+y+z+d)
def division():
    try:
        no1=int(input('enter no'))
        no2=int(input('enter no'))
        print(no1+no2)
    except:
        print('give no')

    finally:
        print('hi')
        division()

division()
def division():
    try:
        no1=int(input('enter no'))
        no2=int(input('enter no'))
        print(no1+no2)
    except:
        print('give no')

    finally:
        print('hi')
        division()

division()
import os,sys
filename=('D:/python/iam.txt')
if os.path.isfile(filename):
    f=open(filename,'r')
    print('file is present')
    linecount=wordcount=charcount=0
    for line in  f:
        #print(line)
        w=line.split()
        wordcount=wordcount+len(w)
        linecount+=1

import csv
with open('D:/python/student.csv','w',newline='') as file:
    reynolds=csv.writer(file)
    reynolds.writerow(['srd','snname','stuaddress'])
    count=int(input('enter no of students'))
    for i in range(count):
        sid=int(input('enter student id'))
        sname=input('enter student name')
        saddress=input('enter address')
        reynolds.writerow([sid,sname,saddress])
import re
def mobileno(sentence):
    mobilenumber=re.compile('(91[6-9][0-9]{9})')
    number=mobilenumber.findall(sentence)
    return number
sentence='my mobile no is 918234567890 and 918888888888,917345678990'
number_present=mobileno(sentence)
print(type(number_present))
for number in number_present:
    print(number)


import random
import time
names=['ganesh','thas','aravinth','vidhya']
colors=['red','blue','green','yellow']
def peoplelist(numpeople):
    result=[]
    for i in range(numpeople):
        student={'id':i,'name':random.choice(names),'team':random.choice(colors)}
        result.append(student)
    return result
def stu(count):
    for i in range(count):
        student = {'id': i, 'name': random.choice(names), 'team': random.choice(colors)}

timer1=time.clock()
r=stu(100000)
timer2=time.clock()
print('time taken is',timer2-timer1)

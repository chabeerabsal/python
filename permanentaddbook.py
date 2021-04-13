import sqlite3
class addressbook:
    def __init__(self):
        self.conttactname=''
        self.emailid=''
        self.address=''

    def givecontactdetails(self):
        self.contactname=input('enter your name')
        self.emailid=input('enter email id')
        self.address=input('enter address')
        return self.contactname,self.emailid,self.address
    def display(self):
        print('contact name:',self.contactname)
        print('email id:',self.emailid)
        print('address:',self.address)
        print('\n')
contactlist=[]
choice='y'

while(choice=='y'):
    print('1.add new contact \n 2.display contacts')
    responce=int(input('enter your choice'))
    if(responce==1):
        contact=addressbook()
        (name,emailid,address)=contact.givecontactdetails()
        #contactlist.append(contact)
        with sqlite3.connect('D:/New folder/sql/addressbook.db') as con:
            cur=con.cursor()
            cur.execute('insert into contactdetails(name,email,address)values(?,?,?)',(name,emailid,address))
            con.commit()
            msg='contact ssuccessfully added'
    elif(responce==2):
        #for x in contactlist:
            #x.display()
        con=sqlite3.connect('D:/New folder/sql/addressbook.db')
        cur=con.cursor()
        cur.execute('select * from contactdetails')
        result=cur.fetchall()
        print(result,sep='\n')
    else:
        print('enter correct choice')
    choice=input("press 'y' to continue")
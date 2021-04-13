class addressbook:
    def __init__(self):
        self.conttactname=''
        self.emailid=''

    def givecontactdetails(self):
        self.contactname=input('enter your name')
        self.emailid=input('enter email id')
    def display(self):
        print('contact name:',self.contactname)
        print('email id:',self.emailid)
        print('\n')
contactlist=[]
choice='y'

while(choice=='y'):
    print('1.add new contact \n 2.display contacts')
    responce=int(input('enter your choice'))
    if(responce==1):
        contact=addressbook()
        contact.givecontactdetails()
        contactlist.append(contact)
    elif(responce==2):
        for x in contactlist:
            x.display()
    else:
        print('enter correct choice')
    choice=input("press 'y' to continue")
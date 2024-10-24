

def filedetail(name,address,email,mob):
    with open (f'{name}.txt','w')as myfile:

        myfile.write(f'name:{name}\n Address:{address}\n Email:{email}\n Mob:{email}\n)
        name = input("enter name")
        address= input("enter the address")
        context3 = input('enter the email')
        context4 = int(input('enter the mob:'))
        

filedetail()


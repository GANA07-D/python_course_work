instagram=eval(input("follows account: "))
if instagram:
    close_friends=eval(input("close friends: "))
    if close_friends:
        print("story visible")
    else:
        print("not close friends list")
else:
    print("follow the account first")



    


reg=eval(input("registration: "))
if reg:
    fee=eval(input("fee paid:"))
    if fee:
        print("Tournament entry confirmed")
    else:
        print("fee is pending:")
else:
    print("register first")






link_active=eval(input("link active: "))
if link_active:
    permission=eval(input("permission granted: "))
    if permission:
        print("file opened successfully")
    else:
        print("access denied")
else:
    print("invalid File Link")


  


data={
    'dipak':{'status':False,'python':None,'mysql':None,'flask':None},
    'teja':{'status':True,'python':99,'mysql':98,'flask':97},
    'dinesh':{'status':True,'python':70,'mysql':74,'flask':67},
    'rasool':{'status':True,'python':20,'mysql':20,'flask':30},
    'babai':{'status':True,'python':77,'mysql':76,'flask':70},
}

name=input("Enter your name: ")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f"hello {name}!!!")
        print(f"your average score is {avg}")
        if avg>=90:
            print("outstanding performance")
        elif avg>=80:
            print("very good")
        elif avg>=70:
            print("Good,work hard")
        elif avg >=35:
            print("better luck next time")
        else:
            print("you failed the exam,try hard")
    else:
        print(f'{name} did not attend the exam ,bring your parents')
else:
    print(f"{name} is not there in data")
        
            
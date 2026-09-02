'''
def functio_name(argument):
    #statement
    return (output)

functionname(parameters)    


def gst(price):
    print("Original Price:",price)
    print("Final Price:",price+price*0.18)
55

gst(1000)
gst(5000)
gst(800)
gst(500)
gst(10000)  



def table(n):
    print(f"{n}-Table")
    print('----------------------------------')
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')


for i in range(1,21):
    table(i)
 


def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap year"
    else:
        return "not a Leap year"

print(isleap(2014))    
print(isleap(2016)) 
print(isleap(2024)) 



def prime(num):
    for i in range(2,num//2+1):
    



def display(name,email,pwd):
    print("name:",name)
    print("email",email)
    print("pwd:",pwd)


display('Dipak','Dipak@gmail','Dipak@123')
display('Dipak@gmail','Dipak@123','Dipak')
display('Dipak@123','Dipak','Dipak@gmail')



def display(name,email,pwd):
    print("name:",name)
    print("email",email)
    print("pwd:",pwd)


display(name='Dipak',email='Dipak@gmail',pwd='Dipak@123')
display(email='Dipak@gmail',pwd='Dipak@123',name='Dipak')
display(pwd='Dipak@123',name='Dipak',email='Dipak@gmail')


def display(name,email,pwd=None):
    print("name:",name)
    print("email",email)
    print("pwd:",pwd)


display('Dipak','Dipak@gmail',)
display('Dipak@gmail','Dipak@123','Dipak')


def display(*names):
    print(names)
display("dinesh")
display("dinesh","teja")
display("dinesh","teja","dipak")
display("dinesh","teja","dipak","vishnu")



def display(*names):
    print(names)
display(n1="dinesh")
display(n1="dinesh",n2="teja")
display(n1="dinesh",n2="teja",n3="dipak")
display(n1="dinesh",n2="teja",n3="dipak",n4="vishnu")

'''
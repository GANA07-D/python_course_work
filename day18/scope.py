'''
def display():
    n=10 #Here n is the local variable 
    print("Inside function:",n)

n=10 #Here n is the global variable 
display()
print("Outside Function:",n)



def display():
    global n #Here i can give global  access in the local variable
    n=10
    print("Inside Function:",n)

n=10  
display()
print("Outside Function:",n)



def display():
    global n #Here i can give global  access in the local variable
    n+=10
    print("Inside Function:",n)

n=10  
display()
print("Outside Function:",n)



def display():
    course = "PFS"
    def update():
        course ="JFS"
        print("Inner Function:",course)
    update()
    print("OUter function:",course)

display()        



def display():
    course = "PFS"
    def update():
        nonlocal course
        course ="JFS"
        print("Inner Function:",course)
    update()
    print("OUter function:",course)

display() 


l = [1,2,3,4,5]
print(max(l))

print = 20
print(max)
#we should not give the function names to the variables it will not work
#if we do that the function will lose the scope 

'''

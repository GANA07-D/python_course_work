#int float complex str list tuple set dict bool

#list dict set when we change the value that are mutable are going to effect the outside 

#list
def display(data):
    data.append(40)
    print("Inside the Function:", data)

data = [10, 20, 30]
display(data)
print("Outside the Function:", data)

#Set
def display(data):
    data.add(40)
    print("Inside the Function:", data)

data = {10, 20, 30}
display(data)
print("Outside the Function:", data)

#Dictionary
def display(data):
    data["age"] = 22
    print("Inside the Function:", data)

data = {"name": "Deepak"}
display(data)
print("Outside the Function:", data)

#Integer 
def display(n):
    n+=10.3
    print("Inside the Function:",n)

n=12
display(n)
print("Outside the Function:",n)


#Float
def display(n):
    n += 10.3
    print("Inside the Function:", n)

n = 12.5
display(n)
print("Outside the Function:", n)

#String
def display(name):
    name += " Yadav"
    print("Inside the Function:", name)

name = "Deepak"
display(name)
print("Outside the Function:", name)

#Tuple
def display(data):
    data += (40,)
    print("Inside the Function:", data)

data = (10, 20, 30)
display(data)
print("Outside the Function:", data)

#Boolean
def display(value):
    value = False
    print("Inside the Function:", value)

value = True
display(value)
print("Outside the Function:", value)

#Frozenset
def display(data):
    data = data.union({40})
    print("Inside the Function:", data)

data = frozenset({10, 20, 30})
display(data)
print("Outside the Function:", data)
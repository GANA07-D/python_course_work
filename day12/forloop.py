#str list tuple set dict range

for variable in sequence:
    statement(s)

#######################################


s="python programming"
for i in s:
    print(i)

#######################################


l=[1,2,3,4,5]
for i in l:
    print(i)


#########################################

prices=[100,200,300,400,500]
for price in prices:
    print(price)


##########################################

names = ["Deepak","Dinesh","Teja","Babai"]
for name in names:
    print(name)


###########################################

d={1:2,2:4,3:6,4:8,5:10}
for i in d:
    print(i)
    print(d[i])

#######################################

range(start,end+1,step):(0,,1)
for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,0,-2):
    print(i)

    

#######################################

s = 'python programming language'
for i in range(len(s)):
    print(i,s[i])


#######################################

s =(456,4567,4567,543,3456)
for i in range(len(s)):
    print(i,s[i])

########################################

s=[6789,6789,6789,7689]
for i in enumerate(s):
    print(i[0],i[1])


d={1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

#########################################

for i in range(1,11):
    if i==5:
        break   
    print(i) 

########################################


for i in range(1,11):
    if i==5:
        continue
    print(i)    



############################################

for i in range(1,11):
    if i==15:
        break
else:
    print("End of the loop") 



##########################################

l=[12,13,14,15,16,18,19]
n=int(input("Enter the number:"))
for i in l:
    if i==n:
        print("Number is found")
        break
else:
    print("Number is not found")



########################################

pin = 1234

for i in range(5):
    epin = int(input("Enter  the pin:"))
    if epin == pin:
        print("phone is Unlocked")
        break
    else:
        print("Invalid pin")
else:
    print("try after 30 seconds")



##########################################

num=int(input("enter the number:"))
if num < 2:
    print("it is not prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("it is not prime number")
            break
    else:
        print("it is a prime number")



#########################################

n=14
for i in range(1,n//2+1):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")



    
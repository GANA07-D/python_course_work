'''
#revese number of 10 to 1 using recursion 
def display(n):
    if n==11:
        return
    display(n+1)
    print(n)#if we keep the print statement after the return it gonna print display condition
display(1)


#To display the string in reverse order 
def display(s,n):
    if n==len(s):
        return
    
    display(s,n+1)
    print(s[n],end="")

display("Codegnan",0)



def display(l,ind):
    if ind == len(l):
        return 
    return l[ind] + display(l,ind+1)

l=[4,23,2,34,28,90]
print(display(l,0))


def display(l):
    if l==0:
        return 0
    return l%10 + display(l//10)

l= 43567
print(display(l))


def display(l):
    if l==1:
        return 1
    return l*display(l-1)
print(display(5))


n=int(input("Enter the Number:"))
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b = 0,1
    print(a,b)
    for i in range(8):
        a,b = b,a+b
        print(b,end="")

'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(20):
    print(fib(i))    
    



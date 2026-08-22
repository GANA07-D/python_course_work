'''

i = 1
while i <= 10:
    print(i)
    i += 1


i = 10
while i>0:
    print(i)
    i -= 1


i = 5
while i <= 50:
    print(i)
    i += 5


s = 'while  loop'
i=0
while i < len(s):
    print(s[i])
    i += 1
   

s = 'while  loop'
i=len(s)-1
while i >= 0:
    print(s[i])
    i -= 1



l=[5467,5678,6789,987]
i=0
while i < len(l):
    print(l[i])
    i += 1


n = int(input('Enter a number to find the sum of its digits in your number: '))
sumofdigits=0
while n>0:
    sumofdigits += n%10
    n=n//10
print(sumofdigits)



n = int(input('Enter a number to find the product of its digits in your number: '))
productofdigits=1
while n>0:
    productofdigits *= n%10
    n=n//10
print(productofdigits)



n=34567

result=0
while n>0:
    
    rem=n%10
    result=result*10+rem
    n=n//10
print(result)


n=int(input('Enter a number to add even digits in your number: '))

result=0
while n>0:
    rem=n%10
    if rem%2==0:
        result += rem
    n=n//10
print(result)


l=[7,9,23,0,0,0,12,0,13,0,1,0,1,4,0,1,0,0,1,1,5,6,6,13,0]
i=len(l)-1
while i>0:
    if l[i]==0:
        l.pop(i)
    i -= 1
print(l)    

l=[7,9,23,0,0,0,12,0,13,0,1,0,1,4,0,1,0,0,1,1,5,6,6,13,0]
i=0
while i < len(l):
    if l[i]==0:
        l.pop(i)
    else:
        i += 1
print(l)      

l=[7,9,23,0,0,0,12,0,13,0,1,0,1,4,0,1,0,0,1,1,5,6,6,13,0]
while 0 in l:
    l.remove(0)
print(l)

'''

l=[2,3,6,76,12,4,5,62,4,5,2,23]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i += 1
    j -= 1
        







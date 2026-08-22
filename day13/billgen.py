'''
data={
    'sugar':50,
    'salt':30,
    'cookingoil':90,
    'chilli power':70,
    'egg':70,
    'peanut':85,
    'rice':130,
    'butter':130,
    'bread':200,
    'wheatflour':100
}
for i in data:
    print(i.ljust(20),data[i])


bill=0
while True:
    product=input("Enter the product name or [E]xit: ")
    if product=='E'or product=='e':
        print("Thanks for shopping")
        print("Total bill: ",bill)
        break
    else:
        quantity=int(input("Enter the quantity :"))
        bill+=data[product]*quantity











products = input("Enter the products:").split()
print("------------Bill------------ ")
bill=0
for i in products:
    print(i.ljust(20),data[i])
    bill+=data[i]
print("Total: ".ljust(20),bill)

##############################################

s = "python programming"

data = {}

for i in s:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

print(data)

########################################

s='aaabbbbbhhhhhwweeeebbbbeerrrllahh'
count=1
result=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        result+=s[i]+str(count)
        count=1
print(result+s[i]+str(count))

'''

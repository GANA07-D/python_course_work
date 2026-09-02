#var = lambda  arg: exp
'''
wish = lambda name: f"welcome to the course {name}"
print(wish("rasool"))
print(wish("ranjith"))

gst = lambda price: price+price*0.18
print(gst(1000))
print(gst(4000))

avg = lambda a,b,c: (a+b+c)/3
print(avg(4,6,8))
print(avg(20,30,50))

iseven = lambda n: "even" if n%2==0 else "odd"
print(iseven(5))
print(iseven(6))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(6,8,10))
print(largest(34,68,44))

isvowel = lambda a: "vowel" if a in 'aeiouAEIOU' else "consonant"
print(isvowel("e"))
print(isvowel("k"))
'''
'''
l = [2,3,4,5,6,7,8,9]
update = list(map(lambda i: i+10,l))
print(update)

t = [123,456,789,234,678]
discount = list(map(lambda i: i-i*0.3,t))
print(discount)
'''
'''
l = [2,3,4,5,6,7,8,9]
update = list(filter(lambda i: i%2!=0,l))
print(update)

t = [123,456,789,234,678]
discount = list(filter(lambda i: i>1000,t))
print(discount)
'''
'''
l=['ranjithkumar@gmail.com','ranjithyaramothu@gmail.com','ranjith@gmail.com','kumar1526@gmail.com']
domain = list(map(lambda i: i.split('@')[-1],l))
print(domain)
'''
'''
from functools import reduce

l = [4,5,6,7,89,24,66,88]
res = reduce(lambda sum,i: sum+i,l)
print(res)

res1 = reduce(lambda pro,i: pro*i,l)
print(res1)
'''
'''
products={'Eggs':80,
          'suger':50,
          'salt':89,
          'butter':100,
          'milk':20
}

res = list(filter(lambda i: products[i]>50,products))
print(res)
'''
products={'Eggs':80,
          'suger':50,
          'salt':89,
          'butter':100,
          'milk':20
}
print(dict(sorted(products.items(),key= lambda i:i[1])))
print(dict(sorted(products.items(),key= lambda i:i[1],reverse=True)))
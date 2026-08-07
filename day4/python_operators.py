Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python operators
'''
1.Arthematic
2.comparison
3.Assignement
4.relation
5.membership
6.identity
7.bitwise
'''
'\n1.Arthematic\n2.comparison\n3.Assignement\n4.relation\n5.membership\n6.identity\n7.bitwise\n'
#arthematic operators
a=10
b=5
a+b
15
a_b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a_b
NameError: name 'a_b' is not defined
a-b
5
a*5
50
a/2
5.0
9/2
4.5
9//2
4
9.5//2
4.0
9.0//2
4.0
10.2//2
5.0
a//2
5
a**3
1000
2**3
8
16**2
256
12%2
0
a%3
1
#comparison operators
a<b
False
a>b
True
a>=10
True
a<=10
True
a==b
False
a!=b
True
#Assignment operators
a=20
a =a+20
a
40
a =+10
a
10
a=+10
a
10
a +=10
a
20
a=50
a +=10
4
a
60
a -=10
a *=20
a
1000
a//=2
a
500
a **=2
a
250000
a /=500
a
500.0
a=100
a %=3
a
1
a +=1
a
2
a=10
a
10
#relational operations
#logical operators
email =true
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    email =true
NameError: name 'true' is not defined. Did you mean: 'True'?
email = True
password = False
email and password
False
email or password
True
login =  True
login = False
display_products = True
login or display_products
True
's' in 'aeiou'
False
not 's' in 'aeiou'
True
7%2==0 and 3%2==0
False
6%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True
3%2==0
False
not 3%2==0
True
#membership operators
#str list tuple set dict
s='python programming'
'python' in s
True
'java' in s
False
'z' in s
False
'c++' not in s
True
'pogramm' not in s
True
'program' not  in s
False
1=[1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,2,3,4,5]
3 in l
True
9 not in l
True
t =(10,20,30,40)
50 in t
False
30 not in t
False
s={'pen','paper','book'}
'book' not in s
False
'bag' not in s
True
'pen' in s
True
data={'name':'dinesh','batch':65,'course':'pfs'}
'dinesh' in data
False
65 in data
False
'batch' in data
True
'age' not in data
True
'dob' in data
False
fuck up
SyntaxError: invalid syntax
'dob' in data
False
'pfs' in data
False
>>> 'course' in data
True
>>> #Identity operators
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> id(l)
2992338569024
>>> id(m)
2992338744512
>>> l ==m
True
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3, 4]
>>> id(n)
2992338744512
>>> m is n
True
>>> n is m
True
>>> n is l
False
>>> n is not l
True
>>> #bitwise operators
>>> 11 & 12
8
>>> 11 | 15
15
>>> 11^12
7
>>> 2<<2
8
>>> 2<<3
16
>>> 2<<4
32
>>> 16<<2
64
>>> ~14
-15
>>> ~78
-79
>>> ~23
-24
>>> ~~32
32
>>> ~~~32
-33

Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float complex str list tuple set dict bool
a = input()
codegnan
a
'codegnan'
a = input()
1234
a
'1234'
a = input("enter the value:")
enter the value:deepak is good boy
a
'deepak is good boy'
marks=input("enter the marks:")
enter the marks:99
marks
'99'
price = float(intput("enter the price:"))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    price = float(intput("enter the price:"))
NameError: name 'intput' is not defined. Did you mean: 'input'?
price = float(input("enter the price:"))
enter the price:123.421
price
123.421
cgpa = float(input("enter the cgpa:"))
enter the cgpa:9.8
cgpa
9.8
#split()
#split()
\
names.split()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
names = ['Dipak',' Teja','Dinesh',' Babai']
names,split()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names,split()
NameError: name 'split' is not defined
names.split()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names.split()
AttributeError: 'list' object has no attribute 'split'
names.split(',')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    names.split(',')
AttributeError: 'list' object has no attribute 'split'
names
['Dipak', ' Teja', 'Dinesh', ' Babai']
names.split(',')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    names.split(',')
AttributeError: 'list' object has no attribute 'split'
names.split
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    names.split
AttributeError: 'list' object has no attribute 'split'
names = ['Dipak',' Teja','Dinesh',' Babai']
names
['Dipak', ' Teja', 'Dinesh', ' Babai']
names
['Dipak', ' Teja', 'Dinesh', ' Babai']
names.split(',')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    names.split(',')
AttributeError: 'list' object has no attribute 'split'
name =input()
name.split()
names = 'Dipak',' Teja','Dinesh',' Babai'
names.split(',')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    names.split(',')
AttributeError: 'tuple' object has no attribute 'split'
courses='python,java,c++,flask'
courses
'python,java,c++,flask'
courses.split
<built-in method split of str object at 0x0000018BC20977B0>
courses.split(',')
['python', 'java', 'c++', 'flask']
softskills ='communication quicklearner'
softskills.split()
['communication', 'quicklearner']
names=input("Enter the names:").split()
Enter the names:deepak teja dinesh 
names
['deepak', 'teja', 'dinesh']
names=set(input("enter the names:").split()

          deepak teja dinesh
          
SyntaxError: '(' was never closed
names=set(input("enter the names:").split())
          
enter the names:Dipak Teja Dinesh Babai
names
          
{'Babai', 'Teja', 'Dipak', 'Dinesh'}
marks = input().split()
          
10 20 30 40 50 
marks
          
['10', '20', '30', '40', '50']
map(int,marks)
          
<map object at 0x0000018BC208B280>
list(map(int,marks))
          
[10, 20, 30, 40, 50]
marks = list(map(int,input("enter the marks").split()))
          
enter the marks12 13 14 15 16 17 18
marks
          
[12, 13, 14, 15, 16, 17, 18]
marks =tuple(map(int,input("enter  the marks:").split()))
          
enter  the marks:98 97 96 95 94 93  92 91 
marks
          
(98, 97, 96, 95, 94, 93, 92, 91)
marks =set(map(int,input("enter  the marks:").split()))
          
enter  the marks:98 97 96 95 94 93  92 91 
marks
          
{96, 97, 98, 91, 92, 93, 94, 95}
prices =set(map(float,input("enter the prices:").split())
            )
          
enter the prices:2000 2345 300.34  11.22
prices
          
{2000.0, 2345.0, 11.22, 300.34}
a,b=[1,2]
          
a
          
1
b
          
2
a,b,c=(1,12.3,"str")
          
a
          
1
b
          
12.3
c
          
'str'
email,password=input("Enter the email ,password:").split()
          
Enter the email ,password:Dipak_Darapu Dipak@123
email
          
'Dipak_Darapu'
password
          
'Dipak@123'
name,marks =input("enter the name and marks:").split()
          
enter the name and marks:Deepak 99
name
          
'Deepak'
marks
          
'99'
int(marks)
          
99
a,b,c=list(map(int,input().split()))
          
22 33 44
a
          
22
b
          
33
c
          
44
status=eval(input())
          
status
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'status' is not defined
status
          
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    status
NameError: name 'status' is not defined
status = eval(input())
          
status = eval(input())
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1
    status = eval(input())
                  ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> status = eval(input())
...           
true
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> status = eval(input())
...           
True
>>> status
...           
True
>>> type(status)
...           
<class 'bool'>
>>> status =eval(input())
...           
2+3J
>>> status
...           
(2+3j)
>>> type(status)
...           
<class 'complex'>
>>> status=eval(input())
...           
[1,2,3,4]
>>> status
...           
[1, 2, 3, 4]
>>> status = eval(input())
...           
(1,2,3,4)
>>> status
...           
(1, 2, 3, 4)
>>> status=eval(input())
...           
{1:1,2:2,3:3,4:4}
>>> status
...           
{1: 1, 2: 2, 3: 3, 4: 4}
>>> type(status)
...           
<class 'dict'>

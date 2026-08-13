Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Dictionaries
#ordered mutable heterogeneous dynamic unique duplication property
#values  can  be mutable can be duplicate BUT--->>> keys must  immutable,unique
d{}
SyntaxError: invalid syntax
d={}
type(d)
<class 'dict'>
d{1:4,2:8,3:13}
SyntaxError: invalid syntax
d={1:4,2:8,3:13}
d
{1: 4, 2: 8, 3: 13}
d
{1: 4, 2: 8, 3: 13}
d={}
d
{}
d={}
d[1}=1
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
d[1]=1
d[12.3]=1
d['str']=1
d[(1,2,4)=1
  
SyntaxError: invalid syntax
d[(1,2,4)]=1
  
d[(2+3j)]=1
  
d[[1,2,3]]=1
  
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[True}=1
  
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
d[True]=1
  
d
  
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
d[False]=1
  
d
  
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1}
d[1]=1
  
d[2]=12.3
  
d[3]='str'
  
d[4]=2+3j
  
d[5]=True
  
d[6]={1,2,3]
  
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d[6]={1,2,3}
  
d[7]=(1,2,3)
  
d[8]={1,2,3}
  
d[9]=frozenset({1,2,3})
  
d{10]={1:1,2:2}
  
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d{10}={1:1,2:2}
  
SyntaxError: invalid syntax
d[10]={1:1,2:2}
  
d[11]=None
  
d
  
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: {1, 2, 3}, 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
d{]
  
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d{}
  
SyntaxError: invalid syntax
d={}
  
d[1]=2
  
d
  
{1: 2}
d[1]=3
  
d
  
{1: 3}
#Dictionary Operations
  
data={'name':'Dipak','course':'pfs','batch':65}
  
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65}
"Dipak" in data
  
False
65 in data
  
False
'course' in data
  
True
data['nname']
  
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    data['nname']
KeyError: 'nname'
data['name']
  
'Dipak'
data['batch']
  
65
data['course']
  
'pfs'
data.get('name')
  
'Dipak'
data.get('batch')
  
65
data.get('age')
  
data.get('age','key is not present')
  
'key is not present'
data.get('batch','key is not present')
  
65
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65}
#Add key value pairs
  
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65}
data['age']=21
  
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21}
data['phone']=9876543210
  
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210}
data.updata({'email':'deepak@gmail..com','py':2026})
  
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    data.updata({'email':'deepak@gmail..com','py':2026})
AttributeError: 'dict' object has no attribute 'updata'. Did you mean: 'update'?
data.update({'email':'deepak@gmail..com','py':2026})
  
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210, 'email': 'deepak@gmail..com', 'py': 2026}
id(data)
  
1522812704128
data['py']
  
2026
data['py']=2027
  
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210, 'email': 'deepak@gmail..com', 'py': 2027}
data['age']=22
  
id(data)
  
1522812704128
data.popitem()
  
('py', 2027)
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone': 9876543210, 'email': 'deepak@gmail..com'}
data.pop('course')
  
'pfs'
data
  
{'name': 'Dipak', 'batch': 65, 'age': 22, 'phone': 9876543210, 'email': 'deepak@gmail..com'}
data.pop('age')
  
22
data.pop('email')
  
'deepak@gmail..com'
data
  
{'name': 'Dipak', 'batch': 65, 'phone': 9876543210}
del data['batch']
  
data
  
{'name': 'Dipak', 'phone': 9876543210}
data.clear()
  
data{}
  
SyntaxError: invalid syntax
data
  
{}
data={'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210, 'email': 'deepak@gmail..com', 'py': 2026}
  
data
  
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210, 'email': 'deepak@gmail..com', 'py': 2026}
len(data)
  
7
data.keys()
  
dict_keys(['name', 'course', 'batch', 'age', 'phone', 'email', 'py'])
data.values(0
            )
  
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    data.values(0
TypeError: dict.values() takes no arguments (1 given)
data.values()
                
dict_values(['Dipak', 'pfs', 65, 21, 9876543210, 'deepak@gmail..com', 2026])
data.items()
                
dict_items([('name', 'Dipak'), ('course', 'pfs'), ('batch', 65), ('age', 21), ('phone', 9876543210), ('email', 'deepak@gmail..com'), ('py', 2026)])
sorted(data)
                
['age', 'batch', 'course', 'email', 'name', 'phone', 'py']
max(data)
                
'py'
min(data)
                
'age'
max(data)
                
'py'
>>> d={1:1,2:2}
...                 
>>> m=d
...                 
>>> m[3}=3
...                 
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> m[3]=3
...                 
>>> m
...                 
{1: 1, 2: 2, 3: 3}
>>> d
...                 
{1: 1, 2: 2, 3: 3}
>>> n=d.copy()
...                 
>>> n[5]=5
...                 
>>> n
...                 
{1: 1, 2: 2, 3: 3, 5: 5}
>>> d
...                 
{1: 1, 2: 2, 3: 3}
>>> data
...                 
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210, 'email': 'deepak@gmail..com', 'py': 2026}
>>> data.get('py')
...                 
2026
>>> data.setdefault('py',2026)
...                 
2026
>>> data
...                 
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210, 'email': 'deepak@gmail..com', 'py': 2026}
>>> data.setdefault('name',2026)
...                 
'Dipak'
>>> data.setdefault('email',2026)
...                 
'deepak@gmail..com'
>>> data.setdefault('key',2026)
...                 
2026
>>> data
...                 
{'name': 'Dipak', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone': 9876543210, 'email': 'deepak@gmail..com', 'py': 2026, 'key': 2026}
>>> dict.fromkeys(["python","mysql","java"],0)
...                 
{'python': 0, 'mysql': 0, 'java': 0}

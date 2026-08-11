Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#continue of string
#whitespace & Trimmimg
s='    hello   world    '
s.strip()
'hello   world'
s.lstrip()
'hello   world    '
s.rstrip()
'    hello   world'
s.replace(' ','')
'helloworld'
#splitting and joining methods
s='java-python-flask-mysql-fastapi-c'
s.split('-')
['java', 'python', 'flask', 'mysql', 'fastapi', 'c']
s.split('-',2)
['java', 'python', 'flask-mysql-fastapi-c']
s.rsplit('-',2)
['java-python-flask-mysql', 'fastapi', 'c']
l='''python'''
l='''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c
NameError: name 'c' is not defined
c="python,java,mysql,flask"
c
'python,java,mysql,flask'
''.join(c)
'python,java,mysql,flask'
','.join(c)
'p,y,t,h,o,n,,,j,a,v,a,,,m,y,s,q,l,,,f,l,a,s,k'
' '.join(c)
'p y t h o n , j a v a , m y s q l , f l a s k'
'@'.join(c)
'p@y@t@h@o@n@,@j@a@v@a@,@m@y@s@q@l@,@f@l@a@s@k'
'-'.join({'1','2','3'})
'1-3-2'
'-'.Join({'1','2','3'})
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    '-'.Join({'1','2','3'})
AttributeError: 'str' object has no attribute 'Join'. Did you mean: 'join'?
'-'.join({'1','2','3'})
'1-3-2'
a='string.py.java.png.txt'
s
'java-python-flask-mysql-fastapi-c'
a
'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
#string testing method
a='string.png'
a.startwith('str')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.startwith('str')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith('str')
True
a.endswith('png')
True
a.endswith('i')
False
>>> 'pythonv.13'.islower()
True
>>> 'Pythonv.13'.islower()
False
>>> 'PYTHON23456'.isupper()
True
>>> 'deepak'.isaplha()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    'deepak'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> 'deepak'.isalpha()
True
>>> 'deepak123'..isalpha()
SyntaxError: invalid syntax
>>> True
... 'deepak123'.isalpha()
SyntaxError: multiple statements found while compiling a single statement
>>> 'deepak123'.isalpha()
False
>>> 'deepak123'.isalnum()
True
>>> '  '.isspace()
True
>>> '    hello'.isspace()
False
>>> 'Hlo Wor'.istitle()
True
>>> 'HLO Word'.istitle()
False
>>> 'my_var'..isidentifier()
SyntaxError: invalid syntax
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> a.partition('.')
('string', '.', 'png')
>>> '2345'.isdecimal()
True
>>> 'wasedrfgyhu'.isdecimal()
False
>>> '4567'.isnumerics()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    '4567'.isnumerics()
AttributeError: 'str' object has no attribute 'isnumerics'. Did you mean: 'isnumeric'?
>>> '4567'.isnumeric
<built-in method isnumeric of str object at 0x00000222E94A2D30>
>>> '4567'.isnumeric()
True

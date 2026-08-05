Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del c
>>> c
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c=40
>>> c
40
>>> del c
>>> a=1
>>> if a==2:
...     print("ok")
... else:
...     print("not ok");
... 
...     
not ok

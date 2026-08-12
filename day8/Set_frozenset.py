Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set
#mu uni dyn  hete unique elements
s=set()
type(s)
<class 'set'>
s={1,2,3,4,5,6,134124,124,2345234,312}
a
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a
NameError: name 'a' is not defined
s
{1, 2, 3, 4, 5, 6, 134124, 2345234, 312, 124}
s={1,1,1,1}
s
{1}
s=set()
s.add(1)
s.add(12.3)
s.add('str")
      
SyntaxError: unterminated string literal (detected at line 1)
s.add("str")
      
s.add([1,2,3])
      
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add(False)
      
s
      
{False, 1, 'str', 12.3}
s.add((1,3,4))
      
s
      
{False, 1, 12.3, (1, 3, 4), 'str'}
#set  operation
      
#set membership operation
      
a={1,2,3,4,5}
      
b={3,5,7,8,9}
      
2 in a
      
True
10 not in a
      
True
a|b
      
{1, 2, 3, 4, 5, 7, 8, 9}
a&b
      
{3, 5}
a-b
      
{1, 2, 4}
b-a
      
{8, 9, 7}
a^b
      
{1, 2, 4, 7, 8, 9}
a

a
      
{1, 2, 3, 4, 5}
#{1}(1,2}{1,2,3,5},[4,5}{4,5,6}
      
a
      
{1, 2, 3, 4, 5}
{1}<=a
      
True
{1,2,3}<=a
      
True
{1,7,8,9}<=a
      
False
a>=[1,2}
      
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a>={1,2}
      
True
a>={15,16}
      
False
m={1,2,3}
      
n={4,5,6}
      
n.isdisjoint(m)
      
True
a.isdisjoint(b)
      
False
#set methods
      
a
      
{1, 2, 3, 4, 5}
a={12,43,1,7,89,40,23,44}
      
a
      
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
      
[1, 7, 12, 23, 40, 43, 44, 89]
max(a)
      
89
min(a)
      
1
len(a)
      
8
a.index(a)
      
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
all({1,1,23,43,13,1})
      
True
any({0,''})
      
False
any({0,'',(),True})
      
True
sum(a)
      
259
a
      
{1, 7, 40, 43, 12, 44, 23, 89}
a{1,2,3}
      
SyntaxError: invalid syntax
a={1,2,3}
      
b=a
      
b.add(4)
      

a
      
{1, 2, 3, 4}
b
      
{1, 2, 3, 4}
c=a.copy()
      
c
      
{1, 2, 3, 4}
c.add(5)
      
c
      
{1, 2, 3, 4, 5}
a
      
{1, 2, 3, 4}
a.add(5)
      
a
      
{1, 2, 3, 4, 5}
a.add(100)
      
a
      
{1, 2, 3, 4, 5, 100}
a.add(40)
      
a
      
{1, 2, 3, 4, 5, 100, 40}
a.add(101)
      
a
      
{1, 2, 3, 4, 5, 100, 101, 40}
a.update({10,20,30,40,})
...       
>>> a
...       
{1, 2, 3, 4, 5, 100, 101, 40, 10, 20, 30}
>>> a.pop()
...       
1
>>> a.pop()
...       
2
>>> a.pop()
...       
3
>>> 
>>> a
...       
{4, 5, 100, 101, 40, 10, 20, 30}
>>> a.remove(101)
...       
>>> a
...       
{4, 5, 100, 40, 10, 20, 30}
>>> a.remove(101)
...       
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.remove(101)
KeyError: 101
>>> a
...       
{4, 5, 100, 40, 10, 20, 30}
>>> a.discard(100)
...       
>>> a
...       
{4, 5, 40, 10, 20, 30}
>>> a.discard(30)
...       
>>> a
...       
{4, 5, 40, 10, 20}
>>> 
>>> a.clear()
...       
>>> a
...       
set()
>>> a=frozenset({1,2,3,4})
...       
>>> a
...       
frozenset({1, 2, 3, 4})

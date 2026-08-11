Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
l=list()
type(l)
<class 'list'>
l=[1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8j]
l
[1, 12.3, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (3+8j)]
l=[1,1,1,1]
l
[1, 1, 1, 1]
#concations
a=[1,2,3]
b=[4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a=[567,76,13,433,134,234]
a
[567, 76, 13, 433, 134, 234]
#indexing
a[1]
76
a[3]
433
a[-5]
76
a[-4]
13
a
[567, 76, 13, 433, 134, 234]
a[1:4]
[76, 13, 433]
a[::-1]
[234, 134, 433, 13, 76, 567]
a[1::2]
[76, 433, 234]
a
[567, 76, 13, 433, 134, 234]
76 in a
True
8765 in a
False
13 not in a
False
13 in a
True
#list methods
a
[567, 76, 13, 433, 134, 234]
max(a)
567
min(a)
13
sorted(a)
[13, 76, 134, 234, 433, 567]
len(a)
6
a
[567, 76, 13, 433, 134, 234]
id(a)
2307525459712
a[0]]
SyntaxError: unmatched ']'
a[0]
567
a
[567, 76, 13, 433, 134, 234]
a[0]=56
id(a)
2307525459712
a[3]=43
a
[56, 76, 13, 43, 134, 234]
a[-1]=23
a
[56, 76, 13, 43, 134, 23]
id(a)
2307525459712
a.append(50)
a
[56, 76, 13, 43, 134, 23, 50]
a.append(60)
a
[56, 76, 13, 43, 134, 23, 50, 60]
a..insert(1,66)
SyntaxError: invalid syntax
a.insert(1,66)
a
[56, 66, 76, 13, 43, 134, 23, 50, 60]
q.extend([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    q.extend([1,2,3,4])
NameError: name 'q' is not defined
a.extend([1,2,3,4])
a
[56, 66, 76, 13, 43, 134, 23, 50, 60, 1, 2, 3, 4]
a
[56, 66, 76, 13, 43, 134, 23, 50, 60, 1, 2, 3, 4]
a.pop()
4
a
[56, 66, 76, 13, 43, 134, 23, 50, 60, 1, 2, 3]
a.pop(0)
56
a.pop(5)
23
a
[66, 76, 13, 43, 134, 50, 60, 1, 2, 3]
a.pop(2)
13
a.remove(23)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.remove(23)
ValueError: list.remove(x): x not in list
a.remove(13)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.remove(13)
ValueError: list.remove(x): x not in list
a
[66, 76, 43, 134, 50, 60, 1, 2, 3]
a.remove(43)
a
[66, 76, 134, 50, 60, 1, 2, 3]
del a[1]
a.clear()
a
[]
id(a)
2307525459712
a
[]
a=[66,13,50,60,14,1]
a.index(13)
1
a
[66, 13, 50, 60, 14, 1]
>>> del a[0:3]
>>> a
[60, 14, 1]
>>> a.index(13)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.index(13)
ValueError: list.index(x): x not in list
>>> a.index(14)
1
>>> a
[60, 14, 1]
>>> a.count(14)
1
>>> a=[1,2,3,4]
>>> b=a
>>> b
[1, 2, 3, 4]
>>> b.append(7)
>>> a
[1, 2, 3, 4, 7]
>>> c=a.copy()
>>> c.append(12)
>>> a
[1, 2, 3, 4, 7]
>>> c
[1, 2, 3, 4, 7, 12]
>>> any([1,'',False,[],(),{},set6()])
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    any([1,'',False,[],(),{},set6()])
NameError: name 'set6' is not defined. Did you mean: 'set'?
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
>>> all([1,'',False,[],(),{},set()])
False
>>> all([0,'',False,[],(),{},set()])
False
>>> sum(a)
17
>>> l.sort()
>>> l
[1, 1, 1, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4, 7]
>>> a.reverse()
>>> a
[7, 4, 3, 2, 1]

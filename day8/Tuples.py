Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Tuples
>>> t=()
>>> t=tuple()
>>> t
()
>>> t=(1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> t=(1)
>>> #to enter single element
>>> t=(1,)
>>> t
(1,)
>>> #tuple can  allow duplication
>>> t=(1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> #tuple is heterogeneous
>>> t=(1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
>>> t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
>>> type(t)
<class 'tuple'>
>>> #tuple concatenation
>>> (1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> #tuple repetation
>>> (1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> #tuple inedexing
>>> t=(1,23.4,'str',[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
>>> t[1]
23.4
>>> t[-3]
{1, 2, 3}
>>> t[2]
'str'
>>> t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
>>> #tuple membership
>>> 23.4 in t
True
>>> 'str' in t
True
>>> False in t
False
>>> #Tuple operations
>>> # are done
>>> 
>>> 
>>> #tuples methods
sorted(t)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t(12,789,32,13,76,32,453,123,7898,1321,32)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t(12,789,32,13,76,32,453,123,7898,1321,32)
TypeError: 'tuple' object is not callable
t=(12,789,32,13,76,32,453,123,7898,1321,32)
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
sorted(t)
[12, 13, 32, 32, 32, 76, 123, 453, 789, 1321, 7898]
max(t)
7898
min(t)
12
len(t)
11
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
t.index(32)
2
t.count(32)
3
all((1,2,3,))
True
any((1,2,3,0,0,0))
True
all((1,2,3,00,0))
False
t=1,2,3
t
(1, 2, 3)
a,b,c=t
a
1
b
2
c
3
t
(1, 2, 3)
t=(1,2,3,4,[1,2,3],5)
t
(1, 2, 3, 4, [1, 2, 3], 5)
t[4]
[1, 2, 3]
4[4].append95)
SyntaxError: unmatched ')'
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t=(1,2,34,4)
sum(t)
41

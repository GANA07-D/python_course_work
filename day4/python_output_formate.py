Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#output formating
#comma separation formate
a=10
b=12.3
c='codegnan'
a
10
b
12.3
c
'codegnan'
print(a,b,c)
10 12.3 codegnan
print("a=",a,"b=",b,"c=",c)
a= 10 b= 12.3 c= codegnan
print("a="a,"b="b,"c="c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("a=",a,"b=",b,"c=",c,sep='')
a=10b=12.3c=codegnan
print("a=",a,"b=",b,"c=",c,sep='\n')
a=
10
b=
12.3
c=
codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t')
a=	10	b=	12.3	c=	codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t',end='\n\n')
a=	10	b=	12.3	c=	codegnan

>>> print("a=",a,"b=",b,"c=",c,sep='\t',end='@')
a=	10	b=	12.3	c=	codegnan@
>>> #f-string formate
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.3 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.300000 c=codegnan
>>> print('a={} b={] c=[]'.formate (a,b,c))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('a={} b={] c=[]'.formate (a,b,c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print('a={} b={] c=[]'.format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print('a={} b={] c=[]'.format(a,b,c))
ValueError: expected '}' before end of string
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print('a={} b={} c={}'.format(b,a,c))
a=12.3 b=10 c=codegnan
>>> print('a={0} b={1} cv={2}'.formate(a,b,c))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('a={0} b={1} cv={2}'.formate(a,b,c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print('a={0} b={1} cv={2}'.formate(a,b,c))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print('a={0} b={1} cv={2}'.formate(a,b,c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print('a={0} b={1} c={2}'.formate(a,b,c))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print('a={0} b={1} c={2}'.formate(a,b,c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print('a={2} b={0} c={1}'.formate(a,b,c))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print('a={2} b={0} c={1}'.formate(a,b,c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=codegnan b=10 c=12.3

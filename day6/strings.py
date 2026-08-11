Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string operations
#concatenation
#repetition
#indexing
#slicing


#concatentation
d="deepak"
d
'deepak'
type(d)
<class 'str'>
a="python"
b="programming"
a+b
'pythonprogramming'
fname="Deepak"
lname=" Darapu"
fname+lname
'Deepak Darapu'
#repetition
a
'python'
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
"*"*20
'********************'
"-codegnan-"*5
'-codegnan--codegnan--codegnan--codegnan--codegnan-'
#indexing
s="codegnan"
s[7]
'n'
s[2]
'd'
s[0]
'c'
s[4]
'g'
s[-1]
'n'
names
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'fname'?
names="Deepak Dinesh Teja Babai Rasuool"
names[:6]
'Deepak'
name[7:13]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    name[7:13]
NameError: name 'name' is not defined. Did you mean: 'fname'?
names[7:13}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
names[7:13]
'Dinesh'
names[14:18]
'Teja'
names[19:23]
'Baba'
names[19:24]
'Babai'
names[-7;]
SyntaxError: invalid syntax
names[-7:]
'Rasuool'
names[-13:-8]
'Babai'
names[-1:-8:-1]
'loousaR'
names[:6:-1]
'loousaR iabaB ajeT hseniD'
names[1:6:-1]
''
names[1:-1:6]
'eD BR'
names[::-8]
'lieD'
"Deepak" in names
True
"Dinesh" in names
True
"rajesh" in names
False
"u"  in names
True
names[13:7:-1]
' hseni'
names[14:7:-1]
'T hseni'
names[11:7:-1]
'seni'
len(names)
32
ord('a')
97
ord('V')
86
ord('A')
65
ord('G')
71
chr(100)
'd'
chr('40')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    chr('40')
TypeError: 'str' object cannot be interpreted as an integer
chr('20')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    chr('20')
TypeError: 'str' object cannot be interpreted as an integer
chr(40)
'('
sorted(names)
[' ', ' ', ' ', ' ', 'B', 'D', 'D', 'R', 'T', 'a', 'a', 'a', 'a', 'a', 'b', 'e', 'e', 'e', 'e', 'h', 'i', 'i', 'j', 'k', 'l', 'n', 'o', 'o', 'p', 's', 's', 'u']
max(names)
'u'
min(names)
' '
names
'Deepak Dinesh Teja Babai Rasuool'
names.upper()
'DEEPAK DINESH TEJA BABAI RASUOOL'
names.lower()
'deepak dinesh teja babai rasuool'
names.swapcase
<built-in method swapcase of str object at 0x000001470392E5B0>
names.swapcase()
'dEEPAK dINESH tEJA bABAI rASUOOL'
names.lower
<built-in method lower of str object at 0x000001470392E5B0>
names.lower()
'deepak dinesh teja babai rasuool'
names.swapcase()
'dEEPAK dINESH tEJA bABAI rASUOOL'
names
'Deepak Dinesh Teja Babai Rasuool'
names.capaitalize()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    names.capaitalize()
AttributeError: 'str' object has no attribute 'capaitalize'. Did you mean: 'capitalize'?
names.capitalize
<built-in method capitalize of str object at 0x000001470392E5B0>
names.capitalize()
'Deepak dinesh teja babai rasuool'
names.title
<built-in method title of str object at 0x000001470392E5B0>
names.title()
'Deepak Dinesh Teja Babai Rasuool'
#alignment
s="Deepak"
s.center(50,'-')
'----------------------Deepak----------------------'
s.center(50,'*')
'**********************Deepak**********************'
s.center(40,'.')
'.................Deepak.................'
s.ljust(40.'.')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.ljust(40,'.')
'Deepak..................................'
s.rjust(40,'.')
'..................................Deepak'
'123'.zfill(4)
'0123'
'123456'.zfill(5)
'123456'
#searching method
names
'Deepak Dinesh Teja Babai Rasuool'
s
'Deepak'
s="python pogramming language"
s.find('python')
0
s.find("p")
0
s.find("P")
-1
sfind("l")
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    sfind("l")
NameError: name 'sfind' is not defined
s.find("l")
18
s.rfind("l")
18
s.rfind("z")
-1
s.inedx("a")
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    s.inedx("a")
AttributeError: 'str' object has no attribute 'inedx'. Did you mean: 'index'?
s.index("a")
11
>>> s.rindex("a")
23
>>> s.count('a')
3
>>> s.count('z')
0
>>> s.count('a,p,g')
0
>>> #replace
>>> s.replace('o','l')
'pythln plgramming language'
>>> s.replace('m','2')
'python pogra22ing language'
>>> s.replace('pythom','java')
'python pogramming language'
>>> s.replace('python','java')
'java pogramming language'
>>> s.maketrans('aeiou','@#$%^')
{97: 64, 101: 35, 105: 36, 111: 37, 117: 94}
>>> s.tanslate((s.maketrans('aeiou','@#$%^'))
... 
...            s
...            
SyntaxError: '(' was never closed
>>> s.tanslate((s.maketrans('aeiou','@#$%^')))
...            
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    s.tanslate((s.maketrans('aeiou','@#$%^')))
AttributeError: 'str' object has no attribute 'tanslate'. Did you mean: 'translate'?
>>> s.tanslate((s.maketrans('aeiou','@#$%^'))
...            l
...            
SyntaxError: '(' was never closed
>>> s.tanslate(s.maketrans('aeiou','@#$%^'))
...            
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    s.tanslate(s.maketrans('aeiou','@#$%^'))
AttributeError: 'str' object has no attribute 'tanslate'. Did you mean: 'translate'?
>>> s.translate(s.maketrans('aeiou','@#$%^'))
...            
'pyth%n p%gr@mm$ng l@ng^@g#'
>>> text="hello🙂"
...            
>>> text.encode()
...            
b'hello\xf0\x9f\x99\x82'
>>> b'hello\xf0\x9f\x99\x82'.decode()
...            
'hello🙂'

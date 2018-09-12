Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'spam eggs'
'spam eggs'
>>> "doesn't"
"doesn't"
>>> '"yes," they said.'
'"yes," they said.'
>>> "\"yes,\" they said."
'"yes," they said.'
>>> '"isn\'t," they said.'
'"isn\'t," they said.'
>>> print('"isn\'t," they said.')
"isn't," they said.
>>> s = 'first line.\nSecond line.'
>>> s
'first line.\nSecond line.'
>>> print(s)
first line.
Second line.
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
>>> print("""\
Usage: thingy [OPTION]
	-h
	-H hostname
""")
Usage: thingy [OPTION]
	-h
	-H hostname

>>> 3* 'un' + 'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
>>> text =
SyntaxError: invalid syntax
>>> text = ('kita terserah akan memaasukan tulisan apa saja.')
>>> text
'kita terserah akan memaasukan tulisan apa saja.'
>>> prefix = 'Py'
>>> prefix 'thon'
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
>>> word= 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> 2word[-2]
SyntaxError: invalid syntax
>>> word[-2]
'o'
>>> word[-6]
'P'
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word{4:]
SyntaxError: invalid syntax
>>> word[:4] + word[4:]
'Python'
>>> word[:2]
'Py'
>>> word[4:]
'on'
>>> word[-2:]
'on'
>>> word[42]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    word[42]
IndexError: string index out of range
>>> word[4:42]
'on'
>>> word[42:]
''
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    word[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'y'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    word[2:] = 'y'
TypeError: 'str' object does not support item assignment
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>> s + 'supercalifragilisticexpialidocius'
'first line.\nSecond line.supercalifragilisticexpialidocius'
>>> len(s)
24
>>> 

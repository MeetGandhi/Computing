Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> int x
SyntaxError: invalid syntax
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(x)
NameError: name 'x' is not defined
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(x)
NameError: name 'x' is not defined
>>> 8%7
1
>>> 4/6*3
0
>>> 4*(3/6)
0
>>> 4//4
1
>>> 6//4
1
>>> 1000//3
333
>>> 1000///3
SyntaxError: invalid syntax
>>> 
>>> 4./6*3
2.0
>>> 4/6.*3
2.0
>>> 
>>> 4/6*3.
0.0
>>> "1"+"2"
'12'
>>> 1+"2"
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    1+"2"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 1.0+2.0
3.0
>>> 1.0+2
3.0
>>> 1 + "2"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    1 + "2"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> "8" + "8"
'88'
>>> type('88')
<type 'str'>
>>> "1" * "2"
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    "1" * "2"
TypeError: can't multiply sequence by non-int of type 'str'
>>> 1.0 * 2
2.0
>>> 1.0 *2.0
2.0
>>> 1 * "2"
'2'
>>> print "1" + "2"
12
>>> "1" * "2"
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    "1" * "2"
TypeError: can't multiply sequence by non-int of type 'str'
>>> 3 * "2"
'222'
>>> 100 * "100"
'100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100100'
>>> 1 / "2"
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    1 / "2"
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> "1" / "2"
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    "1" / "2"
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 100000000000000 * "1190109999999999999999999990"
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    100000000000000 * "1190109999999999999999999990"
MemoryError
>>> not(1==2)
True
>>> t>g
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t>g
NameError: name 't' is not defined
>>> 't' > 'g'
True
>>> 'ttttttttt' > 'tttttt'
True
>>> 'ttttt' > 122
True
>>> 'tttttt' > 0
True
>>> 'j' > 1
True
>>> 'j' >= 1
True
>>> 'j' =1
SyntaxError: can't assign to literal
>>> 'j' = 43
SyntaxError: can't assign to literal
>>> 

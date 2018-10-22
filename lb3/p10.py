Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> fruit="banana"
>>> fruit[1:]
'anana'
>>> fruit[:4]
'bana'
>>> fruit[:dfsdf]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fruit[:dfsdf]
NameError: name 'dfsdf' is not defined
>>> fruit[:8989]
'banana'
>>> fruit[:]
'banana'
>>> string="hello world"
>>> string
'hello world'
>>> string[0]=J
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    string[0]=J
NameError: name 'J' is not defined
>>> string[0]="j"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    string[0]="j"
TypeError: 'str' object does not support item assignment
>>> 
>>> st="Hello World"
>>> print "J",st[1:]
J ello World
>>> print"j"+st[1:]
jello World
>>> new=st.upper()
>>> print new
HELLO WORLD
>>> 

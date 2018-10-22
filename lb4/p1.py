Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> m='meet'
>>> h=list(m)
>>> print h
['m', 'e', 'e', 't']
>>> t=['pining','me','up']
>>> delimiter='-'
>>> delimiter.join(t)
'pining-me-up'
>>> b=delimiter.join(t)
>>> b
'pining-me-up'
>>> t.split(delimiter)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t.split(delimiter)
AttributeError: 'list' object has no attribute 'split'
>>> b.split(delimiter)
['pining', 'me', 'up']
>>> 

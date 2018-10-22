Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> lst=[1,2,9,8]
>>> lst[1]=7# hence list is mutable
>>> lst
[1, 7, 9, 8]
>>> fruit="banana"
>>> fruit[4]=m
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    fruit[4]=m
NameError: name 'm' is not defined
>>> fruit[4]="m"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fruit[4]="m"
TypeError: 'str' object does not support item assignment#hence string is not mutable
>>> tup=1,2,"mrrt"
>>> tup[1]=5
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tup[1]=5
TypeError: 'tuple' object does not support item assignment#hence tuple is not mutable to not allow to rewrite
>>> 

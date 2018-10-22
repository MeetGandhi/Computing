Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> tup=1,5,3,6
>>> tup[3]
6
>>> len(tup)
4
>>> fruit="banana"
>>> print fruit[1]
a
>>> print[10]
[10]
>>> print fruit[10]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print fruit[10]
IndexError: string index out of range
>>> print fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print fruit[1.5]
TypeError: string indices must be integers, not float
>>> print fruit[-2] #[length-2]
n
>>> print fruit[-100]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print fruit[-100]
IndexError: string index out of range
>>> print fruit[len(fruit)]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print fruit[len(fruit)]
IndexError: string index out of range
>>> 

Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> tup="me", "mee", "meet", ""
>>> print tup[0]
me
>>> print tup[3]

>>> print tup[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print tup[5]
IndexError: tuple index out of range
>>> 
input testscore out of 50=-9
input labscore out of 50=-6
grade=D+
>>> len(tup)
4
>>> s[1:3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s[1:3]
NameError: name 's' is not defined
>>> tup[1:3]
('mee', 'meet')
>>> tup[0:3]
('me', 'mee', 'meet')
>>> tup[1:5454454545]
('mee', 'meet', '')
>>> string="meet gandhi"
>>> string[1:445456456]
'eet gandhi'
>>> string[2:5]
'et '
>>> 

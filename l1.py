Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> t=(1,2,34)
>>> t[0]=0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    t[0]=0
TypeError: 'tuple' object does not support item assignment
>>> t=([1,2,3,4,5],77777)
>>> t[0][3]=555
>>> t
([1, 2, 3, 555, 5], 77777)
>>> s=[1,2,3,4,"meet"]
>>> d=dict.fromkeys(s)
>>> d
{1: None, 2: None, 3: None, 4: None, 'meet': None}
>>> f={2:"adfg"}
>>> f.update
<built-in method update of dict object at 0x7f8d825ee050>
>>> f.update(d)
>>> f
{1: None, 2: None, 3: None, 4: None, 'meet': None}
>>> d={3:4,8:7,6:7}
>>> sorted(d)
[3, 6, 8]
>>> lst=d.values()
>>> lst.sort()
>>> lst
[4, 7, 7]
>>> del d[0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    del d[0]
KeyError: 0
>>> del d[3]
>>> d
{8: 7, 6: 7}
>>> del d[7]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    del d[7]
KeyError: 7
>>> d.clear()
>>> d
{}
>>> 

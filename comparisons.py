Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="Meet"
>>> s1="meet"
>>> s<s1
True
>>> s2="gandhi"
>>> s2<s1
True
>>> s3="12456"
>>> s3<s1
True
>>> s4="#$uty"
>>> s4<s3
True
>>> s4<s1
True
>>> l="#"
>>> l1="%"
>>> 1>l1
False
>>> l<l1
True
>>> ord("#")
35
>>> ord("%")
37
>>> ord(1)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
>>> ord("1")
49
>>> ord(" ")
32
>>> l3=" meet"
>>> l3<l1
True
>>> 

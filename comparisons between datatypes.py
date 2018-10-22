Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1<""
True
>>> 2636646<""
True
>>> {1:2,3:4}>30494857
True
>>> []>83748378374
True
>>> ()>23123123123
True
>>> $>21321321
SyntaxError: invalid syntax
>>> # numeric data type is the smallest
>>> {}<""
True
>>> []>{}
True
>>> ()>""
True
>>> # "D"ictionary<"S"tring(d<s)
>>> # "L"ist>"D"ictionary(l>d)
>>> # hence in comparison between tuples,string,dictionary,lists and others,the first word of the datatype is taken into considerationbut not when numeric data type is included as numeric is the first
>>> 

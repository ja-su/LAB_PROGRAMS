Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input()
1000
'1000'
>>> x=intpvf
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x=intpvf
NameError: name 'intpvf' is not defined
>>> x=input()
1009
>>> xx
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    xx
NameError: name 'xx' is not defined
>>> x
'1009'
>>> x=input("enter you roll number")
enter you roll number 10
>>> x
' 10'
>>> y=input("enter name")
enter name jasu
>>> y
' jasu'
>>> 
>>> type(x)
<class 'str'>
>>> 
>>> type(y)
<class 'str'>
>>> x=int(input("enter your roll number"))
enter your roll number20
>>> type(x)
<class 'int'>
>>> m=input("enter your marks")
enter your marks45.5
>>> type(m)
<class 'str'>
>>> m=float(input("enter your marks"))
enter your marks 45.5
>>> type(m)
<class 'float'>
>>> 
<class 'str'>
SyntaxError: invalid syntax
>>> print(m)
45.5
>>> print(y)
 jasu
>>> print(m,y)
45.5  jasu
>>> 

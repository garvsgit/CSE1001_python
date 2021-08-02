Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> newtuple=1,2,3
>>> type(newtuple)
<class 'tuple'>
>>> newtuplw=
SyntaxError: invalid syntax
>>> newtuplw=1
>>> type(newtuple)
<class 'tuple'>
>>> nwetuple=(1)
>>> type(newtuple)
<class 'tuple'>
>>> newtuple=(1)
>>> type(newtuple)
<class 'int'>
>>> newtuple=(1,)
>>> type(newtuple)
<class 'tuple'>
>>> len(newtuple)
1
>>> newtuple=(1,2,3)
>>> newtuple=(,)
SyntaxError: invalid syntax
>>> newtuple=(1,,)
SyntaxError: invalid syntax
>>> newtuple=(1,None)
>>> type(newtuple)
<class 'tuple'>
>>> len(newtuple)
2
>>> newtuple[2]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    newtuple[2]
IndexError: tuple index out of range
>>> newtuple[1]
>>> print(newtuple[1])
None
>>> None
>>> id(newtuple)
1951119741184
>>> newtuple=(1,2,3,)
>>> newtuple
(1, 2, 3)
>>> newtuple=(1,,3)
SyntaxError: invalid syntax
>>> numlist=[1,2,3]
>>> numlist[-1:len(numlist)]
[3]
>>> numlist[-1:-len(numlist)]
[]
>>> numlist[-1:-len(numlist):-1]
[3, 2]
>>> numlist[-1:-len(numlist)-1:-1]
[3, 2, 1]
>>> tup=((1,2),(3,4),(5,6))
>>> tup
((1, 2), (3, 4), (5, 6))
>>> tup[0]
(1, 2)
>>> tup=(1,2,3)
>>> a,b,c=tup
>>> a
1
>>> b
2
>>> c
3
>>> tup=(1,2)
>>> a,b,c=tup
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c=tup
ValueError: not enough values to unpack (expected 3, got 2)
>>> tup=(1,2,3,4)
>>> a,b,c=tup
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a,b,c=tup
ValueError: too many values to unpack (expected 3)
>>> tup=1,
>>> type(tup)
<class 'tuple'>
>>> tup=a,b,c
>>> tup
(1, 2, 3)
>>> print(tup)
(1, 2, 3)
>>> tup.sort(x)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    tup.sort(x)
AttributeError: 'tuple' object has no attribute 'sort'
>>> sorted(tup)
[1, 2, 3]
>>> reversed(tup)
<reversed object at 0x000001C647CAEB50>
>>> *0x000001C647CAEB50
SyntaxError: can't use starred expression here
>>> a=reversed(tup)
>>> a
<reversed object at 0x000001C647CAE520>
>>> list(reversed(tup))
[3, 2, 1]
>>> tuple(reversed(tup))
(3, 2, 1)
>>> sorted(x,reverse=True)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    sorted(x,reverse=True)
NameError: name 'x' is not defined
>>> sorted(tup,reverse=True)
[3, 2, 1]
>>> tup.copy()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    tup.copy()
AttributeError: 'tuple' object has no attribute 'copy'
>>> list(reversed("Hi"))
['i', 'H']
>>> str(reversed("Hi"))
'<reversed object at 0x000001C647CE24C0>'
>>> reversed("Hi")
<reversed object at 0x000001C647CE24C0>
>>> str(list(reversed("Hi")))
"['i', 'H']"
>>> list(reversed({1,2,3}))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list(reversed({1,2,3}))
TypeError: 'set' object is not reversible
>>> set((reversed(tup)))
{1, 2, 3}
>>> str1='abc'
>>> a=tup(str1)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a=tup(str1)
TypeError: 'tuple' object is not callable
>>> a=tuple(str1)
>>> print(a)
('a', 'b', 'c')
>>> type(a)
<class 'tuple'>
>>> type(str1)
<class 'str'>
>>> a is str1
False
>>> type({})
<class 'dict'>
>>> a={1,2,3}
>>> type(a)
<class 'set'>
>>> type("")
<class 'str'>
>>> 5.__sizeof__()
SyntaxError: invalid syntax
>>> tup=()
>>> tup.__sizeof__()
24
>>> __sizeof__(int())
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    __sizeof__(int())
NameError: name '__sizeof__' is not defined
>>> a=5
>>> a.__sizeof__()
28

>>> getsizeof(a)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    getsizeof(a)
NameError: name 'getsizeof' is not defined
>>> sys.getsizeof(a)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    sys.getsizeof(a)
NameError: name 'sys' is not defined
>>> import sys
>>> sys.getsizeof(a)
28
>>> a=[]
>>> sys.getsizeof(a)
56
>>> sys.version()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    sys.version()
TypeError: 'str' object is not callable
>>> b=(1,2,3)
>>> a=tuple(b)
>>> a
(1, 2, 3)
>>> type(a)
<class 'tuple'>
>>> type(b)
<class 'tuple'>
>>> a is b
True
>>> a=b
>>> a is b
True
>>> a=[]
>>> b=[]
>>> a is b
False
>>> b=list(a)
>>> a is b
False
>>> b=a
>>> a is b
True
>>> c=[1,2,3,4]
>>> d=(1,2,3,4)
>>> c.__sizeof__()
104
>>> d.__sizeof__()
56
>>> x-['a','b']
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    x-['a','b']
NameError: name 'x' is not defined
>>> x=['a','b']
>>> x.__sizeof__()
56
>>> y=(a,b)
>>> y=('a','b')
>>> y.__sizeof__()
40
>>> 
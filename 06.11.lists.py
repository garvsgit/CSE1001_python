Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numlist=[123456]
>>> numlist=[1,2,3,4,5,6]
>>> print(numlist)
[1, 2, 3, 4, 5, 6]
>>> numlist[3]=4
>>> numlist[3]="hi"
>>> print(numlist)
[1, 2, 3, 'hi', 5, 6]
>>> numlist[-2:-1]=6,10
>>> print(numlist)
[1, 2, 3, 'hi', 6, 10, 6]
>>> numlist.append(11)
>>> numlist=[1, 2, 3, 'hi', 5, 6]
>>> numlist[-2:-1]=88,99
>>> print(numlist)
[1, 2, 3, 'hi', 88, 99, 6]
>>> numlist[-2]=55
>>> print(numlist)
[1, 2, 3, 'hi', 88, 55, 6]
>>> numlist.remove(6)
>>> print(numlist)
[1, 2, 3, 'hi', 88, 55]
>>> numlist.pop()
55
>>> print(numlist)
[1, 2, 3, 'hi', 88]
>>> del numlist[3:5]
>>> print (numlist)
[1, 2, 3]
>>> numlist[-2]=[10,20]
>>> print(numlist)
[1, [10, 20], 3]
>>> numlist(2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    numlist(2)
TypeError: 'list' object is not callable
>>> numlist[2]
3
>>> numlist[1]
[10, 20]
>>> numlist.pop(1)
[10, 20]
>>> numlist=none
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    numlist=none
NameError: name 'none' is not defined
>>> numlist.clear
<built-in method clear of list object at 0x0000025425725B80>
>>> numlist.clear()
>>> print(numlist)
[]
>>> numlist[1234]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    numlist[1234]
IndexError: list index out of range
>>> numlist=[1,2,3,4]
>>> print(numlist)
[1, 2, 3, 4]
>>> numlist=None
>>> print(numlist)
None
>>> numlist=[]
>>> print(numlist)
[]
>>> numlist(1)=5
SyntaxError: cannot assign to function call
>>> numlist[1]=5
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    numlist[1]=5
IndexError: list assignment index out of range
>>> numlist=[1,2,3,4,5,6]
>>> print(numlist)
[1, 2, 3, 4, 5, 6]
>>> z=numlist
>>> print(z)
[1, 2, 3, 4, 5, 6]
>>> y=z.copy
>>> print(y)
<built-in method copy of list object at 0x00000254286E7C40>
>>> y=z.copy()
>>> print(y)
[1, 2, 3, 4, 5, 6]
>>> a=(1,2,3)
>>> print(a)
(1, 2, 3)
>>> a[1]=5
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a[1]=5
TypeError: 'tuple' object does not support item assignment
>>> z[2]=55
>>> print(z)
[1, 2, 55, 4, 5, 6]
>>> z.count(55)
1
>>> x.cpoy
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x.cpoy
NameError: name 'x' is not defined
>>> z.copy
<built-in method copy of list object at 0x00000254286E7C40>
>>> z.copy()
[1, 2, 55, 4, 5, 6]
>>> newlist=a
>>> newlist[2]=5
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    newlist[2]=5
TypeError: 'tuple' object does not support item assignment
>>> newlist-list(newlist)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    newlist-list(newlist)
TypeError: unsupported operand type(s) for -: 'tuple' and 'list'
>>> newlist1=list(newlist)
>>> print(newlist)
(1, 2, 3)
>>> pritn(newlist1)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    pritn(newlist1)
NameError: name 'pritn' is not defined
>>> print(newlist1)
[1, 2, 3]
>>> list('abc123')
['a', 'b', 'c', '1', '2', '3']
>>> f={a,b,c}
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    f={a,b,c}
NameError: name 'b' is not defined
>>> f={1,2,3}
>>> print(f)
{1, 2, 3}
>>> f[1]='H'
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    f[1]='H'
TypeError: 'set' object does not support item assignment
>>> newlist1[1:]
[2, 3]
>>> m=list(''12'34')
SyntaxError: invalid syntax
>>> x=["a","b","c"]
>>> print(z)
[1, 2, 55, 4, 5, 6]
>>> print(x)
['a', 'b', 'c']
>>> x[len(x)]='d'
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x[len(x)]='d'
IndexError: list assignment index out of range
>>> x=list("abc")
>>> print(x)
['a', 'b', 'c']
>>> x.extend('d')
>>> x.extend(4)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    x.extend(4)
TypeError: 'int' object is not iterable
>>> x.extend((1,2,3))
>>> print(x)
['a', 'b', 'c', 'd', 1, 2, 3]
>>> len(x)
7
>>> g=[5,6,7,,,]
SyntaxError: invalid syntax
>>> f[1]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    f[1]
TypeError: 'set' object is not subscriptable
>>> x
['a', 'b', 'c', 'd', 1, 2, 3]
>>> x.reverse
<built-in method reverse of list object at 0x00000254286E0140>
>>> x.reverse()
>>> x
[3, 2, 1, 'd', 'c', 'b', 'a']
>>> x
[3, 2, 1, 'd', 'c', 'b', 'a']
>>> z
[1, 2, 55, 4, 5, 6]
>>> x.append(z)
>>> x
[3, 2, 1, 'd', 'c', 'b', 'a', [1, 2, 55, 4, 5, 6]]
>>> z=x+5
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    z=x+5
TypeError: can only concatenate list (not "int") to list
>>> z=x+(11,22)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    z=x+(11,22)
TypeError: can only concatenate list (not "tuple") to list
>>> x.sort()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    x.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> x=[1,2,3,4,5,6]
>>> x=[5,6,9,5]
>>> x.sort()
>>> x
[5, 5, 6, 9]
>>> x.sort(reverse=True)
>>> x
[9, 6, 5, 5]
>>> x=[1.2,5.6,9,1]
>>> x.sort
<built-in method sort of list object at 0x0000025428627BC0>
>>> ()
()
>>> x.sort()
>>> x
[1, 1.2, 5.6, 9]
>>> x=list("fahjsfjksahfhf")
>>> x.sort()
>>> x
['a', 'a', 'f', 'f', 'f', 'f', 'h', 'h', 'h', 'j', 'j', 'k', 's', 's']
>>> x=list("hjkfwrjksdhafjkah  fs aff A a ")
>>> x.sort()
>>> x
[' ', ' ', ' ', ' ', ' ', ' ', 'A', 'a', 'a', 'a', 'a', 'd', 'f', 'f', 'f', 'f', 'f', 'h', 'h', 'h', 'j', 'j', 'j', 'k', 'k', 'k', 'r', 's', 's', 'w']
>>> [' ', ' ', ' ', ' ', ' ', ' ', 'A', 'a', 'a', 'a', 'a', 'd', 'f', 'f', 'f', 'f', 'f', 'h', 'h', 'h', 'j', 'j', 'j', 'k', 'k', 'k', 'r', 's', 's', 'w']
[' ', ' ', ' ', ' ', ' ', ' ', 'A', 'a', 'a', 'a', 'a', 'd', 'f', 'f', 'f', 'f', 'f', 'h', 'h', 'h', 'j', 'j', 'j', 'k', 'k', 'k', 'r', 's', 's', 'w']
>>> x.randomize()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    x.randomize()
AttributeError: 'list' object has no attribute 'randomize'
>>> random.shuffle(x)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    random.shuffle(x)
NameError: name 'random' is not defined
>>> import random
>>> random.shuffle(x)
>>> x
['k', 'r', ' ', 'A', ' ', 'f', 'a', ' ', 'f', 'h', ' ', 's', 'f', 'a', 'j', 'j', ' ', ' ', 'f', 'k', 'h', 'a', 's', 'd', 'k', 'a', 'f', 'h', 'w', 'j']
>>> random.shuffle(x)
>>> z
[1, 2, 55, 4, 5, 6]
>>> x
['k', 'a', 'k', 'h', ' ', ' ', ' ', ' ', 'w', 'a', 'j', 'f', 'k', 'f', 'a', 'f', 'f', 'f', 's', 'a', ' ', 'h', 'j', 'd', 'j', 's', 'r', 'A', 'h', ' ']
>>> sorted(x)
[' ', ' ', ' ', ' ', ' ', ' ', 'A', 'a', 'a', 'a', 'a', 'd', 'f', 'f', 'f', 'f', 'f', 'h', 'h', 'h', 'j', 'j', 'j', 'k', 'k', 'k', 'r', 's', 's', 'w']
>>> x.sort
<built-in method sort of list object at 0x0000025428512DC0>
>>> x.sort()
>>> x
[' ', ' ', ' ', ' ', ' ', ' ', 'A', 'a', 'a', 'a', 'a', 'd', 'f', 'f', 'f', 'f', 'f', 'h', 'h', 'h', 'j', 'j', 'j', 'k', 'k', 'k', 'r', 's', 's', 'w']
>>> random(x)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    random(x)
TypeError: 'module' object is not callable
>>> issorted(x)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    issorted(x)
NameError: name 'issorted' is not defined
>>> x=None
>>> x
>>> x=[]
>>> x
[]
>>> type(x)
<class 'list'>
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    x[0]
IndexError: list index out of range
>>> if(x[0]):
	print("Hi")

	
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    if(x[0]):
IndexError: list index out of range
>>> if(x)
SyntaxError: invalid syntax
>>> x=[]
>>> if(x):
	print("Not an empty list")
else:
	print("Empty list")

	
Empty list
>>> list(None)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    list(None)
TypeError: 'NoneType' object is not iterable
>>> x=[]
>>> print(x)
[]
>>> len(x)
0
>>> x=None
>>> len(x)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    len(x)
TypeError: object of type 'NoneType' has no len()
>>> print(x.clear)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print(x.clear)
AttributeError: 'NoneType' object has no attribute 'clear'
>>> print(x.clear()
      )
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    print(x.clear()
AttributeError: 'NoneType' object has no attribute 'clear'
>>> print(x.clear())
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    print(x.clear())
AttributeError: 'NoneType' object has no attribute 'clear'
>>> x=[1,2,3]
>>> print(x.clear())
None
>>> x
[]
>>> x=[1,2]
>>> print(x.sort())
None
>>> x
[1, 2]
>>> x[1:1]
[]
>>> x.extend(
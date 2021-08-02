Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> newset={5,4,3,2,1}
>>> print(newset)
{1, 2, 3, 4, 5}
>>> print(type(newset))
<class 'set'>
>>> x={}
>>> type(x)
<class 'dict'>
>>> x=set()
>>> type(x)
<class 'set'>
>>> x
set()
>>> print(x)
set()
>>> nset={1,2,3,'a','b','c'}
>>> nset
{'a', 1, 2, 3, 'b', 'c'}
>>> type(nset)
<class 'set'>
>>> print(nset)
{'a', 1, 2, 3, 'b', 'c'}
>>> for i in nset:
	print(i)

	
a
1
2
3
b
c
>>> print(sorted(nset))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(sorted(nset))
TypeError: '<' not supported between instances of 'int' and 'str'
>>> newset
{1, 2, 3, 4, 5}
>>> print(sorted(newset))
[1, 2, 3, 4, 5]
>>> newset={1,4,7,2,5,6}
>>> print(sorted(newset)
      )
[1, 2, 4, 5, 6, 7]
>>> newset={1,4,7,2,5,6}
>>> print(sorted(newset))
[1, 2, 4, 5, 6, 7]
>>> 5 in newset
True
>>> 3 not in newset
True
>>> 5 not in newset
False
>>> newset.add(6)
>>> newset
{1, 2, 4, 5, 6, 7}
>>> newset.add([4,3,5])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    newset.add([4,3,5])
TypeError: unhashable type: 'list'
>>> newset.update([9,10,8])
>>> newset
{1, 2, 4, 5, 6, 7, 8, 9, 10}
>>> newset.add({1,2})
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    newset.add({1,2})
TypeError: unhashable type: 'set'
>>> newset.add((1,2))
>>> newset
{1, 2, (1, 2), 4, 5, 6, 7, 8, 9, 10}
>>> for i in newset:
	print(i)

	
1
2
(1, 2)
4
5
6
7
8
9
10
>>> newset.remove((1,2))
>>> newset
{1, 2, 4, 5, 6, 7, 8, 9, 10}
>>> newset.remove((1,2))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    newset.remove((1,2))
KeyError: (1, 2)
>>> newset.remove(1)
>>> newset.remove(1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    newset.remove(1)
KeyError: 1
>>> newset.discard(2)
>>> newset
{4, 5, 6, 7, 8, 9, 10}
>>> newset.discard(4)
>>> newset
{5, 6, 7, 8, 9, 10}
>>> newset.discard(4)
>>> newset.discard(4)
>>> newset.discard(4)
>>> newset.discard(4)
>>> newset.discard(4)
>>> newset
{5, 6, 7, 8, 9, 10}
>>> newset.pop()
5
>>> newset
{6, 7, 8, 9, 10}
>>> newset.pop()
6
>>> newset
{7, 8, 9, 10}
>>> newset.pop()
7
>>> newset
{8, 9, 10}
>>> newset.clear
<built-in method clear of set object at 0x000002223E2A5120>
>>> newset.clear()
>>> newset
set()
>>> del newset
>>> newset
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    newset
NameError: name 'newset' is not defined
>>> newset=set(('redbluegreen'))
>>> newset
{'e', 'u', 'r', 'g', 'b', 'l', 'n', 'd'}
>>> newset=set(('rgb'))
>>> newset
{'b', 'r', 'g'}
>>> len(newset)
3
>>> x
set()
>>> x.union({1,2,3})
{1, 2, 3}
>>> x
set()
>>> x=x.union({1,2,3})
>>> x
{1, 2, 3}
>>> x+{1,2}
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    x+{1,2}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> x.union([1,2])
{1, 2, 3}
>>> x.union([4,5,6])
{1, 2, 3, 4, 5, 6}
>>> x.union("Hello")
{'e', 1, 2, 3, 'l', 'H', 'o'}
>>> x.add("Hello")
>>> x
{1, 2, 3, 'Hello'}
>>> x.remove("Hello")
>>> x
{1, 2, 3}
>>> x
{1, 2, 3}
>>> x.update("Hello")
>>> x
{1, 2, 3, 'e', 'l', 'H', 'o'}
>>> x.add("Hello")
>>> x
{1, 2, 3, 'e', 'l', 'H', 'o', 'Hello'}
>>> x={1,2,3,4,5,6}
>>> y={3,4,5,7,8,9}
>>> x.intersection(y)
{3, 4, 5}
>>> x.intersection_update(y)
>>> x
{3, 4, 5}
>>> x.union_update(y)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    x.union_update(y)
AttributeError: 'set' object has no attribute 'union_update'
>>> i={'a','b','c','d','e','f'}
>>> j={'a','b'}
>>> i
{'a', 'e', 'b', 'f', 'c', 'd'}
>>> i.intersection_update(j)
>>> i
{'a', 'b'}
>>> i={'a','b','c','d','e','f'}
>>> i.differece(j)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    i.differece(j)
AttributeError: 'set' object has no attribute 'differece'
>>> i.difference(j)
{'e', 'f', 'c', 'd'}
>>> i
{'a', 'e', 'b', 'f', 'c', 'd'}
>>> i.intersection_update(j)
>>> i
{'a', 'b'}
>>> i={'a','b','c','d','e','f'}
>>> i.difference_update(j)
>>> 
>>> i
{'e', 'f', 'c', 'd'}
>>> x={"aaa","bbb"}
>>> x
{'aaa', 'bbb'}
>>> x.update({"ccc"})
>>> x
{'aaa', 'ccc', 'bbb'}
>>> x.update(["aaa","ccc"])
>>> x
{'aaa', 'ccc', 'bbb'}
>>> x.update(["aaa","ccc","ddd"])
>>> x
{'aaa', 'ccc', 'ddd', 'bbb'}
>>> x.update(("aaa"))
>>> x
{'aaa', 'a', 'ddd', 'bbb', 'ccc'}
>>> x.update(("xyz"))
>>> x
{'aaa', 'a', 'x', 'ddd', 'bbb', 'ccc', 'z', 'y'}
>>> x={1,2,3,4}
>>> y={5,6,7,8}
>>> x.isdisjoint(y)
True
>>> x={1,2,3,4}
>>> y={1,2,3,4}
>>> x.issubset(y)
True
>>> y.issubset(x)
True
>>> x.issuperset(y)
True
>>> x.syymetricdifference(y)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    x.syymetricdifference(y)
AttributeError: 'set' object has no attribute 'syymetricdifference'
>>> x.symmetricdifference(y)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x.symmetricdifference(y)
AttributeError: 'set' object has no attribute 'symmetricdifference'
>>> x.symmetric_difference(y)
set()
>>> x.symmetric_difference_update(y)
>>> x
set()
>>> x={1,2,3}
>>> x
{1, 2, 3}
>>> y=x
>>> y
{1, 2, 3}
>>> y.add(5)
>>> y
{1, 2, 3, 5}
>>> x
{1, 2, 3, 5}
>>> x is y
True
>>> y=x.copy()
>>> y is x
False
>>> y=x
>>> y is x
True
>>> y=set(x)
>>> y is x
False
>>> a={1,2,3,4,5,6,7,8,9,10}
>>> b={2,4,6,8,10}
>>> a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a&b
{2, 4, 6, 8, 10}
>>> a-b
{1, 3, 5, 7, 9}
>>> b-a
set()
>>> a^b
{1, 3, 5, 7, 9}
>>> b^a
{1, 3, 5, 7, 9}
>>> a^b==b^a
True
>>> a==b
False
>>> a!=b
True
>>> a={1,2,3,4,5,6,7,8,9,10}
>>> b={2,4,6,8,10}
>>> a!=b
True
>>> b<a
True
>>> b<=a
True
>>> b>a
False
>>> a={1,2,3}
>>> b={4,5,6}
>>> a<=b
False
>>> a>b
False
>>> x
{1, 2, 3, 5}
>>> x.update((("Hi")))
>>> x
{1, 2, 3, 5, 'i', 'H'}
>>> x.update(["Hi"])
>>> x
{1, 2, 3, 5, 'Hi', 'i', 'H'}
>>> x{1,2,3}
SyntaxError: invalid syntax
>>> x={1,2,3}
>>> y={1,2,3}
>>> x<y
False
>>> x<=y
True
>>> x.issubset(y)
True
>>> x=(1,2,3)
>>> x.add(4)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    x.add(4)
AttributeError: 'tuple' object has no attribute 'add'
>>> x.append(4)
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    x.append(4)
AttributeError: 'tuple' object has no attribute 'append'
>>> x={1,2,3,4,5,6,7,8,9,0}
>>> y={12}
>>> x.issuperset(y)
False
>>> x>=y
False
>>> x={1,2,3,4,5,6,7,8,9,0}
>>> y={1,2,3,4,5,6,7,8,9,0}
>>> x>=y
True
>>> x>y
False
>>> y={1,2,3,4,5,6,7,8,9}
>>> x>y
True
>>> x>=y
True
>>> x
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> x=frozenset(x)
>>> x
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
>>> type(x)
<class 'frozenset'>
>>> print(x)
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
>>> x.add(4_
      
SyntaxError: invalid decimal literal
>>> x.add(4)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    x.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
>>> const x=5
SyntaxError: invalid syntax
>>> x=5
>>> x=const(x)
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    x=const(x)
NameError: name 'const' is not defined
>>> x=frozen(x)
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    x=frozen(x)
NameError: name 'frozen' is not defined
>>> x
5
>>> x=6
>>> x
6
>>> x={"str1","str2"}
>>> x.update(["str3"])
>>> x
{'str3', 'str2', 'str1'}
>>> x.update(("str3"))
>>> x
{'str3', 's', 'r', 'str2', '3', 'str1', 't'}
>>> x.update(("str3",))
>>> x={"str1","str2"}
>>> x.update(("str3",))
>>> x
{'str3', 'str2', 'str1'}
>>> 
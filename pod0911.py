from collections import OrderedDict
charlist=['a','b','c']
n="".join(OrderedDict.fromkeys(charlist))
print(n)

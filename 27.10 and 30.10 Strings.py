##Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> a="Hello VIT"
##>>> a[-1::-1]
##'TIV olleH'
##>>> a[:6]+"Hi"
##'Hello Hi'
##>>> ch[:8]
##Traceback (most recent call last):
##  File "<pyshell#3>", line 1, in <module>
##    ch[:8]
##NameError: name 'ch' is not defined
##>>> a[:8]+"Hi"
##'Hello VIHi'
##>>> del a
##>>> a
##Traceback (most recent call last):
##  File "<pyshell#6>", line 1, in <module>
##    a
##NameError: name 'a' is not defined
##>>> type(a)
##Traceback (most recent call last):
##  File "<pyshell#7>", line 1, in <module>
##    type(a)
##NameError: name 'a' is not defined
##>>> a="VIT UNIVERSITY"
##>>> print(a)
##VIT UNIVERSITY
##>>> print(a.lower())
##vit university
##>>> print(lower(a))
##Traceback (most recent call last):
##  File "<pyshell#12>", line 1, in <module>
##    print(lower(a))
##NameError: name 'lower' is not defined
##>>> a.isupper()
##True
##>>> a.islower()
##False
##>>> a="VIT UNIVERSITY"
##>>> a="Vit University"
##>>> a.isupper()
##False
##>>> a.islower()
##False
##>>> a="VIT_!@#$%University"
##>>> a.isupper()
##False
##>>> "VIT_!@#$%^&UNIVERSITY"
##'VIT_!@#$%^&UNIVERSITY'
##>>> a.islower()
##False
##>>> a.isupper()
##False
##>>> a="VIT$UNIVERSITY"
##>>> a.isupper()
##True
##>>> a="VIT#UNIVERSITY"
##>>> a.isupper()
##True
##>>> a="VIT_!@#$%University"
##>>> a="VIT_!@#$%University"
##>>> a.isupper()
##>>> 
##>>> a="VIT_!@#$%University"
##>>> a.isupper()
##False
##>>> a="VIT#$%^&UNIVERSITY"
##>>> a.isupper()
##True
##>>> a="VIT_!@#$%^&UNIVERSITY"
##>>> a.isupper()
##True
##>>> "VIT_!@#$%^&UNIVERSITY".isupper()
##True
##>>> "i am Studying BTECH".capitalize()
##'I am studying btech'
##>>> ch="Malayalam"
##>>> ch
##'Malayalam'
##>>> ch.count(a)
##0
##>>> ch.count('a')
##4
##>>> print(" count of ' a in the string ")
## count of ' a in the string 
##>>> ch
##'Malayalam'
##>>> ch=ch.upper()
##>>> ch
##'MALAYALAM'
##>>> ch.count("A",,)
##SyntaxError: invalid syntax
##>>>  ch.count("A",0,5)
## 
##SyntaxError: unexpected indent
##>>> ch.count("A",,)
##SyntaxError: invalid syntax
##>>> ch.count("A",0,5)
##2
##>>> ch="The sun rises in the east"
##>>> ch.find("son")
##-1
##>>> ch.find("sun")
##4
##>>> ch.index("son")
##Traceback (most recent call last):
##  File "<pyshell#53>", line 1, in <module>
##    ch.index("son")
##ValueError: substring not found
##>>> ch.index("sun")
##4
##>>> "Hello VIT".isalpha()
##False
##>>> "HELLOVIT".islapha()
##Traceback (most recent call last):
##  File "<pyshell#56>", line 1, in <module>
##    "HELLOVIT".islapha()
##AttributeError: 'str' object has no attribute 'islapha'
##>>> "HelloBIT".isalpha()
##True
##>>> "Hello BIT".isalphanum()
##Traceback (most recent call last):
##  File "<pyshell#58>", line 1, in <module>
##    "Hello BIT".isalphanum()
##AttributeError: 'str' object has no attribute 'isalphanum'
##>>> "Hello  BIT".isalnum()
##False
##>>> "HelloBIT".isnum()
##Traceback (most recent call last):
##  File "<pyshell#60>", line 1, in <module>
##    "HelloBIT".isnum()
##AttributeError: 'str' object has no attribute 'isnum'
##>>> "HelloBIT".isdigit()
##False
##>>> "465456464".isalpha()
##False
##>>> "323".isdigit()
##True
##2
##>>> "432 234".isdigit()
##False
##>>> max("VIT University")
##'y'
##>>> min("VIT University")
##' '
##>>> "Hello VIT".swapcase()
##'hELLO vit'
##>>> "Hello$VIT".swapcase()
##'hELLO$vit'
##>>> ch="The sun rises in the East"
##>>> ch.startswith("The")
##True
##>>> ch.startwith("sun",4,10)
##Traceback (most recent call last):
##  File "<pyshell#71>", line 1, in <module>
##    ch.startwith("sun",4,10)
##AttributeError: 'str' object has no attribute 'startwith'
##>>> ch.startswith("sun",4,10)
##True
##>>> ch.startswith("sun",8,14)
##False
##>>> ch[8]
##'r'
##>>> ch.startswith("he")
##False
##>>> ch.endswith("st")
##True
##>>> ch.endswith("r",2,9)
##True
##>>> ch[9]
##'i'
##>>> ch.endswith("for",5,8)
##False
##>>> ch.endswith("sun",0,7)
##True
##>>> ch[6]
##'n'
##>>> ch=ch+' '
##>>> ch
##'The sun rises in the East '
##>>> ch.endswith("st")
##False
##>>> ch.endswith("st ")
##True
##>>> 


#Write a python code to replace characters at even postions with @
##a=input()
##for i in range(0,len(a),2):
##    a=a[0:i]+'@'+a[i+1:]
##print(a)


#Write a python code to check the input string is palindrome or not
##a=input()
##a=a.lower()
##b=a[::-1]
##if(b==a):
##    print("Palindrome")
##else:
##    print("Not Palindrome")


#Write a python code to print characters at odd positions of string
##a=input()
##print(a[1::2])

#Write a python code to concatenate two strings character by character
##str1=input()
##str2=input()
##str3=""
##for i in range(0,len(str1)):
##    str3=str3+str1[i]
##for i in range(0,len(str2)):
##    str3=str3+str2[i]
##print(str3)

str1=input()
str2=""
for i in range(len(str1)-1,-1,-1):
    str2=str2+str1[i]
print(str2)

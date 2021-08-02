##def fun():
##    return
##def fun():
##    pass


##def add(a,b):
##    "Returns the sum of two arguments a and b"
##    sum=0
##    sum=a+b
##    return sum
##a=int(input())
##b=int(input())
##add(a,b)

##pi=3.14
##from math import pi
##
##res=0
##
##def area(r):
##    pi=3
##    res=pi*r*r
##    print("Area of Circle",pi)
##
##def circum(r):
##    res=2*pi*r
##    print("Circumference of Circle",pi)
##    return res
##
##
##r=float(input("Radius:"))
##area(r)
###circum(r)
##res=circum(r)
##print("res=",pi)

##def func():
##     var = 100  # A nonlocal variable
##     def func1():
##         
##         def nested():
##             nonlocal var  # Declare var as nonlocal
##             var += 100
##         nested()
##     func1()    
##     
##     print(var)
##
##func()


#enclosing scope
##def ex():
##    a="hi"
##    def eg():
##        b="hello"
##        a="local"
##        print(a)
##        print(b)
##    eg()
##    print(a)
##ex()

##a=0
##def func():
##    b=0
##    def func_1():
##        global a
##        nonlocal b
##        c=10
##        a=5    
##        b=15
##        return c
##    print("c=",func_1())
##    print("b=",b)
##func()
##print("a=",a)
##print("b=",b)

#function using keyword arguments
##def div(b,a):
##    "Division"
##    c=0
##    c=a//b
##    return c
##
##res=div(c=90,b=15)
##print("RESULT:",res)


##def printinfo(c,b,a):
##    print(a,b,c)
##printinfo(10,a=5,b=7)
##printinfo(a=5,b=7,c=10)
##printinfo(a=5,b=7,10)

#function using default arguments
##def div(b, a=180):
##    "Division"
##    c=0
##    c=a//b
##    return c
##res=div(b=15)
##print("Result:",res)

##def printinfo(*vartuple,b,a):
##    "This prints a varibale passed arguments"
####    print(vartuple)
##    vartuple[0]="G"
##    print(b)
##    print(a)
##    print(vartuple)
##    return
##printinfo(30,40,'a','b','c',50,60,'hello',[1,2,3],b=10,a=20)

##def sum(*var):
##    eresult=0
##    oresult=0
##    for x in var:
##        if x%2==0:
##            eresult=eresult+x
##        else:
##            oresult=oresult+x
##    return eresult,oresult
##print(sum(1,2,3,4,5,6))


#Returning multiple values
##def mul_values(m):
##    m.append('dog')
##    return  m
##l=["apple","Ball","Cat"]
##newlist=mul_values(l)
##print(newlist,l,sep=";;;;")


##newlist=[i*4 for i in range(1,6)]
##print(newlist)
##print(*newlist,sep="|")

##
##a=[1,2,3,4,5,6]
##b=['a','b','c','d','e']
##x=list(zip(a,b,a))
##print(x)


##def karg(*k):
##    print(k)
##    return
##karg(a=10,b=20,c=30)


print(pi())

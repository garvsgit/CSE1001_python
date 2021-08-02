#print("Hi!!! This is *** \n\tA First year student \n\t\t currently learning python\n\tHappy Learning friends\nBye!!!")

'''F=float(input())
C=(F-32)/1.8
print(C)
'''

'''
num=12
div=5
rem=num-div*(num//div)
print(rem)
'''

"""
a=5
b=10
'''a=a+b
b=a-b
a=a-b
'''
a=a^b
b=a^b
a=a^b
print("a = ",a,"b = ",b)
"""
'''
#Convert number of days given to years,months,weeks and days. d=int(input("Enter no. of days: "))
d=int(input())
print("Days = ",d)
y=d//365
d=d%365
m=d//30
d=d%30
w=d//7
d=d%7
print("%d Years %d Months %d Weeks %d Days"%(y,m,w,d))
'''
s=int(input())
print("Seconds = ",s)
h=s//3600
s=s%3600
m=s//60
s=s%60
print("%d Hours %d Minutes %d Seconds"%(h,m,s))

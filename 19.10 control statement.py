#break
'''possum=0
negsum=0
n=int(input())
for i in range(n):
    m=int(input())
    if m>0:
        possum=possum+m
    elif m<0:
        negsum=negsum+m
    else:
        break
print("possum=",possum)
print("negsum=",negsum)
'''
'''possum=0
negsum=0
while True:
    m=int(input())
    if m>0:
        possum=possum+m
    elif m<0:
        negsum=negsum+m
    else:
        break
print("possum=",possum)
print("negsum=",negsum)
'''

#continue
'''
word=input()
count=0
for i in word:
    if i==' ':
        continue
    count=count+1
print("Character count =",count)
'''
#pass
'''
word=input()
count=0
for i in word:
    if i==' ':
        pass
    count=count+1
print("Character count =",count)
'''

#Practice Problems
'''if avg>90:
    grade='S'
elif avg>80 and avg<=90:
    grade='A'


if avg>90:
    grade='S'
elif avg>80:
    grade='A'
    '''
'''
n=int(input("enter a number:"))
rev=0
x=n
while(n>0):
    m=n%10
    rev=rev*10+m
    n=n//10
if rev==x:
    print("Yes, It is a palindrome")
else: print("no,It's not a palindrome")

'''

#1,2,4,7,11,...n
##n=int(input())
##i=1
##j=0
##while(i<=n):
##    print(i)
##    j=j+1
##    i=i+j

#FLoyd Triangle
##n=int(input())
##k=1
##for i in range(n):
##    for j in range(i):
##        print(k,end=' ')
##        k+=1
##    print()


#• To print multiplication table from 1 to 10 (print each table upto 20)
##for i in range(1,11):
##    for j in range(1,21):
##        print(i,"*",j,"=",i*j)
##    print("\n\n\n")


#• To check a number is perfect or not
##n=int(input())
##sum=0
##for i in range(1,n):
##    if(n%i==0):
##        sum+=i
##if sum==n:print("Perfect")
##else:print("Not Perfect")


#• To check a number is strong or not (145=1!+4!+5!=145)
##n=int(input())
##t=n
##sum=0
##while(n>0):
##    fact=1
##    m=n%10
##    for i in range(1,m+1):
##        fact=fact*i
##    sum+=fact
##    n=n//10
##if(sum==t):
##    print("Strong")
##else:
##    print("Not Strong")


#• To count no.of vowels and consonants in a given string 
##string=input()
##v=0
##c=0
##for i in string:
##    if(i in "aeiouAEIOU"):v+=1
##    elif(i==' '):pass
##    else:c+=1
##print("V is %d and C is %d"%(v,c))


#• To generate Fibonacci sequence upto n(1,1,2,3,5...n) (use for)
##l=int(input("Enter a number greater than 1"))
##print("Fibonacci upto",l)
##n1=1
##n2=1
##n=0
##print(n1,n2,sep=',',end='')
##
##for i in range(l):
##    n=n1+n2
##    if(n>l):break
##    print(",",n,sep='',end='')
##    n1=n2
##    n2=n

#• To check a number is a prime or not (use for)
##flag=1
##n=int(input())
##if(n not in range(0,3)):
##    for i in range(2,n):
##        if(n%i==0):
##            flag=0
##            break
##if(flag):
##    print("Prime")
##else:
##    print("Not prime")

#To print factorial of a number
##n=int(input())
##fact=1
##for i in range(1,n+1):
##    fact*=i
##print(fact)

#• To print odd numbers upto n (use while)
##n=int(input())
##i=1
##while(i<=n):
##    print(i)
##    i+=2


#• To check the given integer is palindrome or not (use while)
##n=int(input())
##t=n
##rev=0
##while(n>0):
##    rev=rev*10+n%10
##    n=n//10
##if(t==rev):print("Palindrome")
##else:print("Not Palindrome")

#• To print sum of n natural numbers
##sum=0
##n=int(input())
##for i in range(1,n+1):
##    sum+=i
##print(sum)

#Using elseif ladder perform bitwise opertion as per user's choice
op=input("Enter a bitwise operator(&,|,~,^,>>,<<)
n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
if(input=='&'):
   print("n1&n2 =",n1&n2)
elif(input=='|'):
    print("n1|n2 =",n1|n2)
elif(input=='~'):
    print("~n1 =",


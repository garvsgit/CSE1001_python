'''word=input("Enter a String")
print("The letters entered are: ")
for i in word:
    print(i)'''

'''
a=10
print(a,type(a))
a=10.53
print(a,type(a))'''

'''n=int(input("Enter the number of lines"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print()'''

'''n=int(input("Enter the number of lines"))
i=1
while(i<=n):
    j=1
    while j<=i:
        print('*',end='')
        j=j+1
    print()
    i=i+1'''
n=int(input("Enter the number of lines"))
for i in range(1,n+1):
    print("*"*i,end='')
    print()

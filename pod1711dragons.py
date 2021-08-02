a=input()
a=a.split()
s=int(a[0])
n=int(a[1])
dragon=[]
dragontemp=[]
for i in range(n):
    a=input()
    a=a.split()
    dragontemp.append(int(a[0]))
    dragontemp.append(int(a[1]))
    dragon.append(list(dragontemp))
    dragontemp.clear()
for i in range(0,n-1):
    min = i
    for j in range (i+1,n):
        if (dragon[j][0] < dragon[min][0]):
            min = j
    temp = dragon[i]
    dragon[i] = dragon[min]
    dragon[min] = temp   
flag=1
for i in dragon:
    if(i[0]>=s):
        print("NO")
        flag=0
        break
    else:
        s=s+i[1]
if(flag):
    print("YES")

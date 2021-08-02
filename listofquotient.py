import math
n=int(input())
lol=[]
res=[]
for i in range(n):
    m=int(input())
    inp=[]
    for j in range(m):
        inp.append(int(input()))
    lol.append(inp)
p=int(input())
for i in range(n):
    p1=math.prod(lol[i])
    for j in range(i+1,n):
        p2=math.prod(lol[j])
        if p1 > p2:
            q=p1/p2
        else:
            q=p2/p1
        if q <= p:
            res.append((lol[i],lol[j]))
res.sort(key= lambda x:math.prod(x[0]))
print(res)
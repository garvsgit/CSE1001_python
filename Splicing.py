s1=input()
s2=input()
for i in s1:
    for j in s1[s1.index(i)+1:]:
        if(i==j):
            stemp=s1[0:s1.index(i)]+s1[s1.index(i)+1:]
            s1=s1[0:stemp.index(j)+1]+s1[stemp.index(j)+2:]
for i in s2:
    for j in s2[s2.index(i)+1:]:
        if(i==j):
            stemp=s2[0:s2.index(i)]+s2[s2.index(i)+1:]
            s2=s2[0:stemp.index(j)+1]+s2[stemp.index(j)+2:]
  
commoncharlist=[]

for i in s1:
    for j in s2:
        if(i==j):
            commoncharlist.append(i)

crossovers=[]

for i in commoncharlist:
    crossovers.append(s1[0:s1.index(i)]+s2[s2.index(i):])
    crossovers.append(s2[0:s2.index(i)]+s1[s1.index(i):])
    
crossovers.sort()    
for i in crossovers:
    print(i)


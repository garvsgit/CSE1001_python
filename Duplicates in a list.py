n=int(input())
numlist=[int(input()) for i in range(n)]
dup=[]
for i in numlist:
    c=numlist.count(i)
    if c>1 and i not in dup:
        print(i,c,"times")
        dup.append(i)
print(dup)
        

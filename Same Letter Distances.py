w=input()
w=w.lower()
chlist=[chr(i) for i in range(ord('a'),ord('z')+1)]
ocrlist=[0 for i in range(1,27)]
k=0
for j in chlist:
    ocrlist[k]=w.count(j)
    k+=1

pos=ocrlist.index(max(ocrlist))
freqchar=chlist[pos]
print(freqchar)
flag=0
count=0
for i in w:
    if i==freqchar and flag==0:
        flag=1
    elif i==freqchar and flag==1:
        if count-1==0: print("No characters")
        elif count-1==1: print("1 character")
        else: print(count-1,"characters")
        count=0
    if flag==1:
        count+=1
        
    

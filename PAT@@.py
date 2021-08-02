n=int(input())
inputlist=[]
for i in range(n):
    value=int(input())
    inputlist.append(value)
index=int(input())
if(index>=0 and index<n):
    i=index
    while(i<n-1):
        inputlist[i]=inputlist[i+1]
        i+=1
    inputlist=inputlist[:-1]
    for i in inputlist:
        print(i)
else:
    print("Index out of range")


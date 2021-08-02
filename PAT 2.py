n=int(input())
inputlist=[]
deletedlist=[]
for i in range(n):
    value=int(input())
    inputlist.append(value)
index=int(input())
if(index>=0 and index<n):
    deletedlist=list(inputlist)
    i=index
    while(i<n-1):
        deletedlist[i]=deletedlist[i+1]
        i+=1
    i=0
    while(i<n-1):
        inputlist[i]=deletedlist[i]
        print(inputlist[i])
        i+=1
else:
    print("Index out of range")
print(len(deletedlist))

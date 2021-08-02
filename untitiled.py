cute=[]
def tern(n):
    if n == 0:
        return 0
    else:
        e = n//3
        q = n%3
        return tern(e) + str(q)

for i in range (0,387420489):
    temp=tern(i)
    k=2
    cnum=''
    while(k<len(temp)):
        if(temp[k]==0):
            cnum=cnum+'0'
        elif(temp[k]==1):
            cnum=cnum+'8'
        else:
            cnum=cnum+'9'
        k+=1
    cute.append(int(cnum))
cute.reverse()
print(cute)

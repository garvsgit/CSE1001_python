numlist=[5,4,8,1,9,7]
for i in range(0,len(numlist)):
    for j in range(0,i):
        if(numlist[j]>numlist[i]):
            numlist.pop(i)
            numlist.insert(j-1,i)
print(numlist)

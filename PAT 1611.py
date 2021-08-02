inp=input()
inp=inp.split()
numofinputs=int(inp[0])
nthlargest=int(inp[1])
numlist=[]
for i in range(0,numofinputs):
    numlist.append(int(input()))
for i in range(0,nthlargest):
    maximum=numlist[0]
    for j in numlist:
        if j>maximum:
            maximum=j
    numlist.remove(maximum)
print(maximum)

        
        

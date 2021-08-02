n = int(input())
hl = []
vl = []
allLines = []
stairs = []
for i in range(n):
    xstart,ystart = int(input()), int(input())
    xend, yend = int(input()), int(input())
    line=[(xstart,ystart),(xend,yend)]
    allLines.append(line)
    if ystart==yend:
        hl.append(line)
    elif xstart==xend:
        vl.append(line)
allLines.sort()
hl.sort()
vl.sort()
# print(allLines)
# print(hl)
# print(vl)
#sorting so that contiguous lines are formed and the need to check for nearest to origin is eliminated
for l in hl:
    prev='hl'
    flag=0
    s=[l]
    for x in allLines:
        if l[1]==x[0]:
            if (prev=='hl' and x in vl) or (prev=='vl' and x in hl):
                flag=1
                s.append(x)
                l=x
                if(prev=='hl'):
                    prev='vl'
                elif(prev=='vl'):
                    prev='hl'
    if(flag==1):
        stairs.append(s)
lengthofstairs=list(map(len,stairs))
maxlength = max(lengthofstairs)
stairswithmaxlength=[]
for i in stairs:
    if(len(i)==maxlength):
        stairswithmaxlength.append(i)
stairswithmaxlength.sort()
print(*stairswithmaxlength,sep='\n')
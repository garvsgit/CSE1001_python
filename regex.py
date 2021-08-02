import re
inp=input()
flag=-1
x=re.findall("[A-Za-z]+\[[A-Z]+\-\d+\]",inp)
if(not x): print("-1")
else:
    for w in x:
        w=w.replace("["," ")
        w=w.replace("]","")
        print(w)

'''inp=input()
destnum=-1
num=0
for i in inp:
    if(i!='-'):
        num=num*10+int(i)
while(not(destnum>=0 and destnum<=9) or destnum==-1):
    destnum=0
    while(num>0):
        destnum=destnum+num%10
        num=num//10
    num=destnum
print(destnum)

'''
inp=input()
num=0
for i in inp:
    if(i!='-'):
        num=num*10+int(i)
while(True):    
    destnum=0
    while(num>0):
        destnum=destnum+num%10
        num=num//10
    num=destnum
    if(destnum>=0 and destnum<=9):
        break
print(destnum)

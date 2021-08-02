n=int(input())
l=[]
def lsearch(data,key,iteration = 0):
    if data[0] == key:
        return iteration
    elif len(data)>1:
        return lsearch(data[1:],key,iteration+1)
    return None
for i in range(n):
    l.append(int(input()))
value_to_search=int(input())
index=lsearch(l,value_to_search)
if index:
    print(value_to_search,"is present at index",index)
else:
    print(value_to_search,"is not present")

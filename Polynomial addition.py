deg1 = int(input())
coeff1, coeff2 = [], []
for i in range(deg1+1):
    coeff1.append(int(input()))
deg2 = int(input())
for i in range(deg2+1):
    coeff2.append(int(input()))
if deg1 > deg2:
    res = coeff1[0:deg1-deg2]
    for i in range(deg1-deg2, deg1+1):
        res.append(coeff1[i]+coeff2[i-deg1+deg2])
else:
    res = coeff2[0:deg2-deg1]
    for i in range(deg2-deg1, deg2+1):
        res.append(coeff2[i]+coeff1[i-deg2+deg1])
print(res)
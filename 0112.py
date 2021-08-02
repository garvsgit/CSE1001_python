###initialize matrix
##matrix=[]
##def trans(matrix):
##    "Matrix Transpose"
##    for i in range(R):
##        for j in range(C):
##            print(matrix[j][i],end=" ")
##        print()
##    return
##
###Matrix input from user
##R=int(input("Enter the number of rows:"))
##C=int(input("Enter the number of columns:"))
##print("Enter the entries row wise:")
##
##for i in range(R):
##    a=[]
##    for j in range(C):
##        a.append(int(input()))
##    matrix.append(a)
##
###Function call
##trans(matrix)
##

##def matadd(mat1,mat2,r,c):
##    mat3=[]
##    for i in range(r):
##        a=[]
##        for j in range(c):
##            a.append(mat1[i][j]+mat2[i][j])
##        mat3.append(a)
##    return mat3
##a=[[1,2,3],[4,5,6],[7,8,9]]
##b=matadd(a,a,3,3)
##for i in range(3):
##    for j in range(3):
##        print(b[i][j],end=" ")
##    print()
##    

##def matprint(mat,r,c):
##    for i in range(r):
##        for j in range(c):
##            print(mat[i][j], end=" ")
##        print()
##
##def matmul(mat1,mat2,r1,c1,r2,c2):
##    if c1!=r2:
##        return None
##    mat3=[]
##    for i in range(r1):
##        a=[]
##        for j in range(c2):
##            sum=0
##            for k in range(c1):
##                sum=sum+mat1[i][k]*mat2[k][j]
##            a.append(sum)
##        mat3.append(a)
##    return mat3
##mata=[[1,2,3],[4,5,6],[7,8,9]]
##matb=[[1,2,1],[4,3,2],[3,5,4]]
##ans=matmul(mata,matb,3,3,3,3)
##matprint(mata,3,3)
##matprint(matb,3,3)
##matprint(ans,3,3)

            
##def sumn(n):
##    if n==1:
##        return 1
##    total=n+sumn(n-1)
##    return total
##print(sumn(1))
def pp(x):
    if x==0:
        print()
        return
    print('*',end="")
    pp(x-1)
    return
def pat(n):
    if n==0:
        return
    pat(n-1) 
    pp(n)
    return
pat(5)

##n=int(input())
##def pattern(n):
##    if n==0:
##        return
##    else:
##        pattern(n-1)
##    for i in range(n):
##        print('*',end='')
##    print()
##pattern(5)

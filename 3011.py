#Recursion
##def factorial(n):
##    print("Factorial has been called with n =",n)
##    if n==1:
##        return 1
##    else:
##        res = n * factorial(n-1)
##        print("Intermediate result for ",n," * factorial(",n-1,"):",res)
##        return res
##n=int(input("Enter n:"))
##print(factorial(n))

##s='apple','ball','cat','duck','egg','feather','liril','wow'
##x=list(filter(lambda s:len(s),s))
##print(x)


pal=[[0,'a'],[3,'f'],[2,'z'],[9,'m'],[8,'f']]
print(sorted(pal,key=lambda x:x[0]))
print(sorted(pal,key=lambda x:x[1]))


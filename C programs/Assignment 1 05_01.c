//Write a C code to check whether the input number is prime or not using goto
#include<stdio.h>
int main(void)
{
    int n,i=2,flag=1;
    scanf("%d",&n);
    if (n==0 || n==1)
    {
        printf("%d is not a prime number",n);
        return 0;
    }
    else if(n == 2)
    {
        printf("2 is a prime number");
        return 0;
    }
    if (n<0)
    {
        printf("Please enter a positive number");
        return 0;
    }
    prime:
        if(n%i==0)
            flag=0;
        i++;
    if(flag==1 && i<n)
        goto prime;
    if(flag==1)
        printf("%d is a prime number",n);
    else
        printf("%d is not a prime number",n);
    return 0;
}

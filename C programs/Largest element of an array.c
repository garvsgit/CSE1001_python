//4.	Write a C code to print the first prime number that is nearest to the largest number in the array (largest number may be a consonant or prime).
#include<stdio.h>
#include<math.h>
#define n 10
int isPrime(int);
int main(void)
{
    int arr[n]={1,2,3,4,5,6,7,8,9,10};
    int max=arr[0];
    for(int i=0;i<n;++i)
    {
        if(arr[i]>max)
            max=arr[i];
    }
    while(!(isPrime(max)))
    {
        max++;
    }
    printf("%d",max);
    return 0;
}
int isPrime(int x)
{
    int limit=sqrt(x);
    for(int i=2;i<=limit;++i)
    {
        if(x%i==0)
            return 0;
    }
    return 1;
}

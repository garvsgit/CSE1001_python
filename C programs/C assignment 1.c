//1.	Write a C code to print the array in reverse
#include<stdio.h>
#define n 10
int main(void)
{
    int t;
    int a[n]={1,2,3,4,5,6,7,8,9,10};
    for(int i=0, j=n-1;i<n/2;i++,j--)
    {
        t=a[i];
        a[i]=a[j];
        a[j]=t;
    }
    for(int i=0; i<n; ++i)
    {
        printf("%d ",a[i]);
    }
    return 0;
}

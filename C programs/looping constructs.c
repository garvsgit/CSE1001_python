#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int n, sum = 0;
    while(scanf("%d",&n)!=EOF)
        sum=sum+n;
    printf("sum=%d",sum);
}

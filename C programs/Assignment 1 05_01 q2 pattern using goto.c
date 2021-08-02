/*
Write a C code to print the following pattern using goto.

1
12
123
1234
12345
*/
#include<stdio.h>
int main(void)
{
    int n = 0,i = 1,j = 1;
    scanf("%d",&n);
    printf("\n");
    outer:
        j=1;
        inner:
            printf("%d",j);
            j++;
        if (j <= i)
            goto inner;
        printf("\n");
        i++;
    if (i<=n)
        goto outer;
    return 0;
}

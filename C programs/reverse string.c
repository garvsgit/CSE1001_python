//5.	Write a C code to print a line of text in reverse.
#include<stdio.h>
int main(void)
{
    char str[100];
    int i=0;
    printf("Enter your string: ");
    fgets(str,100,stdin);
    for(;str[i]!='\0';++i);
    printf("The reversed string is ");
    for(;i>=0;--i)
    {
        printf("%c",str[i]);
    }
    return 0;
}

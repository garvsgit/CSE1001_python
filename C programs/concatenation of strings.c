#include<stdio.h>
int main(void)
{
    char str1[20],str2[20],con[40];
    fgets(str1,20,stdin);
    fgets(str2,20,stdin);
    int i=0;
    for(i=0;str1[i]!='\0';++i)
    {
        con[i]=str1[i];
        if(str1[i]=='\n')
        {
            break;
        }
    }
    int len=i;
    for(i=0;str2[i]!='\0';++i)
    {
        con[len+i]=str2[i];
        if(str2[i]=='\n')
        {
            break;
        }
    }
    con[i+len]='\0';
    printf("%s",con);
    return 0;

}

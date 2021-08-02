//Q6.	Write a menu driven C code using function.
//1.  to sort a name list using bubble sort  2. To search for a name in the namelist  3.exit
#include<stdio.h>
#include<string.h>
void sort(void);
void search(void);
char strlist[5][20]={"Apple", "Orange", "Banana", "Mango", "Kiwi"};
int main(void)
{
    int choice;
    printf("Enter your choice:\n1 Sort using bubble sort\n2 Search for a name in the namelist \n3 Exit\n");
    scanf("%d",&choice);
    switch(choice)
    {
    case 1:
        sort();
        break;
    case 2:
        search();
        break;
    case 3:
        printf("Exiting...");
        return 0;
        break;
    default:
        printf("Invalid choice. Exiting...");
        return 0;
    }
    return 0;
}
void sort(void)
{
    char temp[20];
    int flag;
    while(1)
    {
        flag=0;
        for(int i=0;i<4;++i)
        {
            if (strcmp(strlist[i],strlist[i+1])>0)
            {
               strcpy(temp,strlist[i]);
               strcpy(strlist[i],strlist[i+1]);
               strcpy(strlist[i+1],temp);
               flag=1;
            }
        }
        if (flag==0)
            break;
    }
    for(int k=0;k<5;++k)
    {
        printf("%s\n",strlist[k]);
    }
}
void search(void)
{
    char toSearch[20];
    int flag=0,i;
    fflush(stdin);
    printf("Enter the name you want to search: ");
    scanf("%[^\n]s",&toSearch);
    for(i=0;i<5;++i)
    {
        if(strcmp(toSearch,strlist[i])==0)
        {
            flag=1;
            break;
        }
    }
    if(flag)
        printf("Element found at index %d",i);
    else
        printf("Element not found");
    return;
}

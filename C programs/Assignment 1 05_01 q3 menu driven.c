/*
Write a menu driven program in C using switch statement and looping constructs to perform the following operations based on user’s choice:
1. Palindrome number
2. perfect number
3. strong number
4. Armstrong number
5. exit
*/
#include<stdio.h>
#include<math.h>
void palin(int);
void perfect(int);
void strong(int);
void armstrong(int);
int fact (int);
int main(void)
{
    int choice=-1,n;
    char anothernum='n';
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("1. Palindrome number\n2. perfect number\n3. strong number\n4. Armstrong number\n5. exit\n");
    scanf("%d",&choice);
    while(choice!=5)
    {
        switch(choice)
        {
        case 1:
            palin(n);break;
        case 2:
            perfect(n);break;
        case 3:
            strong(n);break;
        case 4:
            armstrong(n);break;
        case 5:
            return 0;
            break;
        }
        printf("1. Palindrome number\n2. perfect number\n3. strong number\n4. Armstrong number\n5. exit\n");
        scanf("%d",&choice);
    }
    return 0;
}
int fact(int n)
{
    int factorial=1;
    for(int i=n;i>0;i--)
        factorial*=i;
    return factorial;
}

void palin(int n)
{
    int rev=0,digit,temp = n;
    while(temp>0)
    {
        digit = temp%10;
        temp/=10;
        rev=rev*10+digit;
    }
    if(rev == n)
        printf("%d is a palindrome\n",n);
    else
        printf("%d is not a palindrome\n",n);
}

void perfect(int n)
{
    int sum=0;
    for(int i=1;i<n;++i)
    {
        if(n%i == 0)
            sum+=i;
    }
    if (sum == n)
        printf("%d is a perfect number\n",n);
    else
        printf("%d is not a perfect number\n",n);

}

void strong(int n)
{
    int sum=0,digit,temp = n;
    while(temp>0)
    {
        digit = temp%10;
        temp/=10;
        sum+=fact(digit);
    }
    if(sum == n)
        printf("%d is a strong number\n",n);
    else
        printf("%d is not a strong number\n",n);
}
void armstrong(int n)
{
    int sum=0,digit,temp = n;
    while(temp>0)
    {
        digit = temp%10;
        temp/=10;
        sum+=pow(digit,3);
    }
    if(sum == n)
        printf("%d is an armstrong number\n",n);
    else
        printf("%d is not an armstrong number\n",n);
}

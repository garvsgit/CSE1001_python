//2.	Write a C code to print binary equivalent (base 2) of a decimal number (base 10)
#include<stdio.h>
#include<math.h>
int main(void)
{
    int decimal=0,binary=0,iter=0,num=0;
    scanf("%d",&decimal);
    while(decimal>0)
    {
        num=decimal%2;
        binary=binary+num*pow(10,iter);
        iter++;
        decimal/=2;
    }
    printf("%d",binary);
    return 0;
}
//Alternate
//int main(void)
//{
//    int decimal=0,iter=0;
//    int binary[128];
//    scanf("%d",&decimal);
//    while(decimal>0)
//    {
//        bin[iter]=decimal%2;
//        iter++;
//        decimal/=2;
//    }
//    for(int j=i-1;j>=0;--j)
//    {
//        print("%d",bin[j]);
//    }
//    return 0;
//}

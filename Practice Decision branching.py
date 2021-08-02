#• To print a number is odd or even 
'''a=int(input("Enter a number"))
if(a%2==0):
    print("The number is even")
else:
    print("The number is odd")
'''

'''
#• To check the entered character is a vowel or consonant 
ch=input("Enter a character to check")
if ch in "aeiouAEIOU":
    print("The character is a vowel")
else:
    print("The character is consonant")
'''


#• To check a number is divisible by 4 or not using bitwise operator
'''a=int(input("Enter a number"))
if(a&3==0):
    print("The number is divisible by 4")
else:
    print("The number is not1 divisible by 4")'''

#Alternate
'''a=int(input("Enter a number"))
if((a>>2)<<2==a):
    print("The number is divisible by 4")
else:
    print("The number is not divisible by 4")'''


#• To find smallest of 5 numbers
"""
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))
e=int(input("Enter a number"))
if(a<b and a<c and a<d and a<e):
    print("a is the smallest")
elif(b<c and b<d and b<e):
    print("b is the smallest")
elif(c<d and c<e):
    print("c is the smallest")
elif(d<e):
    print("d is the smallest")
else:
    print("e is the smallest")
"""
#• Write a program to check if a year is leap year or not. 
N=int(input())
if(N%4==0):
            if(N%100==0):
                if(N%400==0):
                    flag=1
                else: flag=0
            else:
                flag=1
else:   
    flag=0
if flag==1:
    print("Leap Year")
else:
    print("Not a Leap Year")

#• Using elseif ladder perform bitwise operation as per user's choice.
'''op=input("Enter the bitwise operation you would like to perform")
a=5
b=10
if(op=='
'''
#• Write a program to find sum of three given integers. However, if any 
#two input values are equal sum will be zero.
##a,b,c=int(input()),int(input()),int(input())
##if(a==b or b==c or c==a):
##    sum=0
##else:
##    sum=a+b+c
##print(sum)

##• Ask user to enter age, sex ( M or F ) , marital status ( Y or N ) and then using following 
##rules print their place of service. 
##if employee is female and age is between 20 to 60, then she will work only in urban areas. 
##if employee is a male and age is in between 20 to 40 then he may work in anywhere 
##if employee is male and age is in between 40 to 60 then he will work in urban areas only. 
##And any other input of age should print 'IERROR".


##• Write a program to input electricity unit charges and calculate total electricity bill 
##according to the given condition: 
##For first 50 units Rs. 0.50/unit 
##For next 100 units Rs. 0.75/unit 
##For next 100 units Rs. 1.20/unit 
##For unit above 250 Rs. 1.50/unit 
##• An additional surcharge of 20% is added to the bill
u=int(input())
if(u<=50):
    cost=0.5*u
elif(u>50 and u<=150):
    cost=50*0.5+(u-50)*0.75
elif(u>150 and u<=250):
    cost=50*0.5+100*0.75+(u-150)*1.20
elif(u>250):
    cost=*0.5+100*0.75+100*1.20+

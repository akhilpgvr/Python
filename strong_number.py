#This is the code for finding strong number using recursion


def fact(n):
    if(n == 1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))
copy=n
sum=0
while(n>0):
    k=n%10                              #Taking each digit of number using modulus operator
    sum=sum+fact(k)                     #Adding sum of factorial of each digit up to number>0
    n=int(n/10)
if(copy == sum):
    print("strong number")
else:
    print("not a strong number")
    

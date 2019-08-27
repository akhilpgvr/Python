#This is the code for perfoming factorial using recursion


def fact(n):
    if(n == 1):
        return 1
    else:
        return n*fact(n-1)                      #recursing statement up to n=1
n=int(input("enter a number"))
print(fact(n))

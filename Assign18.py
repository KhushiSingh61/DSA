def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")
printN(14)
def printNreverse(n):
    if n>0:
        print(n,end=" ")
        printNreverse(n-1)
def printNOdd(n):
    if n>0:
        printNOdd(n-1)
        print(2*n-1,end=' ')
def printNEven(n):
    if n>0:
        printNEven(n-1)
        print(2*n,end=' ')
printNEven(10)
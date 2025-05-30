n = int(input("enter any whole number for which you want to find factorial :"))

def fact(n):

    if (n ==0):
        return 1

    else:

        res = n * fact(n-1)
        return res

factorial = fact(n)

print(factorial)









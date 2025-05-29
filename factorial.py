# n = int(input("enter any whole number for which you want to find factorial :"))

# def fact(n):

#     if (n ==0):
#         return 1

#     else:

#         res = n * fact(n-1)
#         return res

# factorial = fact(n)

# print(factorial)


# n = int(input("enter any whole number for which you want to find factorial :"))
# res = 1

# # if n ==0:
# #     print(f"factorial is {res} ")

# for i in range(1,n+1):

#         res = res*(i)

# print(res)

n = int(input("enter:"))
res =1

while n:        
    res = res*n
    n = n-1
print(res)





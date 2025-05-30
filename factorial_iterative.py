n = int(input("enter any number to which you want to find factorial : "))

result = 1

for i in range(1,n+1):
    result = result*i

print(result)
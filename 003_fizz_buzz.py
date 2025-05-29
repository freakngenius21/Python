for i in range(1,101):
    res = ''
    if (i%3 == 0):
        res += "fizz"
    if (i%5 == 0):
        res += "buzz"
    if (res == ''):
        res = i
    print(res)
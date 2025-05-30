def onetohun(num):
    
    if num <= 100:
        print(num)
        onetohun(num+1)
 
onetohun(1)
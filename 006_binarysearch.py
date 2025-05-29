a = [1, 2, 3, 5, 6, 7, 9, 11, 34, 55, 66, 88, 112, 116, 188, 202, 321]

s = int(input("Enter a number to search whether it is in the array or not: "))

low = 0
high = len(a) - 1


while low <= high:
    mid = (low + high) // 2

    if a[mid] == s:
        print("The number is found at index", mid)
        break
        
    elif a[mid] > s:
        high = mid - 1
    elif a[mid] < s:
        low = mid + 1

else:
    print("The number is not found in the array.")

    
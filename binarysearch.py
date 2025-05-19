a = [1, 2, 3, 5, 6, 7, 9, 11, 34, 55, 66, 88, 112, 116, 188, 202, 321]

s = int(input("Enter a number to search whether it is in the array or not: "))

low = 0
high = len(a) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == s:
        print("The number is found at index", mid)
        found = True
        break
    if a[mid] > s:
        high = mid - 1
    if a[mid] < s:
        low = mid + 1

if not found:
    print("The number is not found in the array.")

    
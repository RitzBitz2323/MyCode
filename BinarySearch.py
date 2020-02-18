def search(array, x):
    num = x
    size = len(array)
    l = 0
    h = size - 1
    mid = l + (h - l) / 2

    if num > array[mid]:
        search(array[mid:])
    elif num < array[mid]:
        search(array[:mid])
    elif num == array[mid]:
        return "Found"
    else:
        return "Not Found"



print("Binary Sort")
array = [1,2,3,4,5,6,7,8,9]
x = int(input("Type in the number you'd like to search for."))
print(search(array, x))
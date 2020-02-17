def search(array, x):
    num = x
    count = 0
    while count < len(array):
        if(num == array[count]):
            return "Found"
        else:
            count = count + 1
    return "Not Found"

print("Linear Sort")
array = [1,2,3,4,5,6,7,8,9]
x = int(input("Type in the number you'd like to search for."))
print(search(array, x))

def sort(array):
    temp = array
    a = 0
    for i in range(a, len(array)):
        temp[i] = min(array[a:len(array)])
        a = a + 1
        i = i + 1

    return array

print("Selection Sort")
array = [1,9,2,5,3,6]
print(sort(array))
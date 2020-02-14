def insertSort(array):
    for i in range(1,len(array)):
        c = array[i]
        while i > 0 and array[i-1] > c:
            array[i] = array[i-1]
            i = i - 1
        array[i] = c
    return array
print("Insertion Sort")
array = [5,13,4,8]
insertSort(array)
print(*array)
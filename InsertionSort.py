def insertSort(array):
    for x in range(0, len(array)):
        temp = array[x]
        count = x
        y = x
        while count > 0:
            count = count - 1
            if array[y] <  array[count]:
                array[y] = array[count]
                array[count] = temp
                y = y - 1
            ##count = count - 1
    return array
print("Insertion Sort")
array = [5,10,4,8,2,9,1,6,3,7]
insertSort(array)
print(*array)
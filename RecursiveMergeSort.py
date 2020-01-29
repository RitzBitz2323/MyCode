def mergeSort(array):
    if(len(array) > 1):
        midpoint = len(array)//2
        left = array[:midpoint]
        right = array[midpoint:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        u = 0

        if(left[i] > right[u]):
            temp = right[u]
            right[u] = left[i]
            left[i] = temp
            i = i + 1
            u = u + 1

        k = 0
        while(k < len(left)):
            array[k] = left[k]
            k = k + 1
        p = 0
        while(p < len(right)):
            array[p] = right[p]
            p = p + 1








print("Recursive Merge Sort")
array = [5,1,2,4,8,3,9,7]
mergeSort(array)
print(*array)
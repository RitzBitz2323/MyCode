def mergeSort(array):
    if(len(array) > 1):
        midpoint = len(array)//2
        left = array[:midpoint]
        right = array[midpoint:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        u = 0
        v = 0
        while(i < len(left) and u < len(right)):
            if(left[i] < right[u]):
                array[v] = left[i]
                i = i + 1
            else:
                array[v] = right[u]
                u = u+1
            v = v + 1
        k = v
        while(i < len(left)):
            array[k] = left[i]
            k = k + 1
            i = i + 1
        while(u < len(right)):
            array[k] = right[u]
            u =  u + 1
            k = k + 1




print("Recursive Merge Sort")
array = [5,1,2,4,8,3,9,7,6]
mergeSort(array)
print(*array)
def mergeSort(array):
    while(len(array)>1):
        middle = len(array)//2 # Finds middle of array
        left = array[:mid]  # Left side of array gets split off
        right= array[mid:]  # Right side of array gets split off

        #while(len(left) > 1 and len(right) > 1):     May use code like this or this exact to make it non recursive

        a = 0
        b = 0
        c = 0

        # Copies data to temporary arrays left [] and right [[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j=j+1
            k=k+1

    print(*array)


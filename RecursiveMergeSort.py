def mergeSort(arr):
    if len(arr) > 1:
        midpoint = len(arr)//2
        leftSide = arr[:midpoint]
        rightSide = arr[midpoint:]

        mergeSort(leftSide)
        mergeSort(rightSide)

        arrayCount = 0
        lsCount = 0
        rsCount = 0
        while lsCount < len(leftSide) and rsCount < len(rightSide):
            if leftSide[lsCount] < rightSide[rsCount]:
                arr[arrayCount] = leftSide[lsCount]
                lsCount = lsCount + 1
            else:
                arr[arrayCount] = rightSide[rsCount]
                rsCount = rsCount + 1
            arrayCount = arrayCount + 1


        while lsCount < len(leftSide):
            arr[arrayCount] = leftSide[lsCount]
            lsCount = lsCount + 1
            arrayCount = arrayCount + 1

        while rsCount < len(rightSide):
            arr[arrayCount] = rightSide[rsCount]
            rsCount = rsCount + 1
            arrayCount = arrayCount + 1


print("Recursive Merge Sort")
arr = [1,5,7,3,2,8,6,4,9]
mergeSort(arr)
print(*arr)
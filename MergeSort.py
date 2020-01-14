def mergeSort(array):
    while(len(array)>1):
        middle = len(array)//2 # Finds middle of array
        left = array[:middle]  # Left side of array gets split off
        right= array[middle:]  # Right side of array gets split off

        #while(len(left) > 1 and len(right) > 1):     May use code like this or this exact to make it non recursive

        i = 0
        j = 0
        k = 0

        # Copies data to temporary arrays left [] and right [[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j=j+1
            k=k+1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()



print("Merge Sort")
a = [5,4,1,2,3,8,6]
print("Initial Array")
printList(a)
print("Sorted Array")
mergeSort(a)
printList(a)

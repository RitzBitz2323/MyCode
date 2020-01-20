def mergeSort(a):
    mid = len(a)//2
    l = a[:mid]
    r = a[mid:]
    i = 0
    if(l[i] > r[i]):
        num = r[i]
        r[i] = l[i]
        l[i] = num
    a[i] = l[i]
    a[i+1] = r[i]
    print(*a)




print("Merge Sort 2 Numbers")
arr = [100,7]
mergeSort(arr)
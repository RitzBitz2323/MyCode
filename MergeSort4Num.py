def mergeSort(a):
    mid = len(a)//2
    leftSide = a[:mid]
    rightSide = a[mid:]
    i = 0
    j = 0
    k = 0
    l = 0

    print(*leftSide)
    print(*rightSide)

    if leftSide[i] > leftSide[i+1]:
        k = leftSide[i+1]
        l = leftSide[i]
        leftSide[i] = k
        leftSide[i+1] = l
    if rightSide[j] > rightSide[j+1]:
        k = rightSide[i+1]
        l = rightSide[i]
        rightSide[i] = k
        rightSide[i+1] = l
    while i < 2:
        a[i] = leftSide[i]
        i = i + 1
    while j < 2:
        a[i] = rightSide[j]
        j = j + 1
        i = i + 1

    print(*leftSide)
    print(*rightSide)
 # ----------- Above Code works and separates array into 2 arrays and that sorts them
    e = 0
    b = 2
    tempa = 0
    tempb = 0
    count = 0
    while count < 4:
        if a[e] > a[b]:
            tempa = a[e]
            tempb = a[b]
            a[e] = tempb
            a[b] = tempa
            if e < 2:
                e = e + 1
        else:
            tempa = a[b]
            tempb = a[e]
            a[e] = tempb
            a[b] = tempa
            if b < 4:
                b = b + 1
        count = count + 1
    p = 1
    if a[p] > a[p+1]:
        tempa = a[p]
        tempb = a[p+1]
        a[p] = tempb
        a[p+1] = tempa






print("Merge Sort 4 Numbers")
arr = [3,1,9,8]
mergeSort(arr)
print(*arr)
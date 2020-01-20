#import pdb
def mergeSort(inputlist):
   # pdb.set_trace()
    mid = len(inputlist)//2
    left = inputlist[:mid]
    right = inputlist[mid:]
    index = 0
    if(left[index] > right[index]):
        num = right[index]
        right[index] = left[index]
        left[index] = num
    inputlist[index] = left[index]
    inputlist[index+1] = right[index]
    print(*inputlist)




print("Merge Sort 2 Numbers")
arr = [100,7]
mergeSort(arr)
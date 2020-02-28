import math
def sort(array, x, h, l, mid):

    if (a[mid] == x):
        return "Found"
    if(len(array) > 1):
        target = x
        a = array[l:h]
        mid = l + ( (target-a[l])*(h-l) / (a[h]-a[l]) )
        mid = int(mid)
        if(x > a[mid]):
            l = mid + 1
            sort(a,x,h,l)
        elif(x < a[mid]):
            h = mid - 1
            sort(a, x, h, l)
        else:
            return "Not Found"
    else:
        if(a[0] == target):
            return "Found"
        else:
            "Not Found"


print("Interpolation Search")
array = [1,3,8,9,13,18,23]
target = 12
l = 0
h = len(array) - 1
mid = l + ( (x-a[l])*(h-l) / (a[h]-a[l]) )
mid = int(mid)
print(sort(array,target,h,l, mid))
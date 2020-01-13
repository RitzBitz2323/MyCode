import pdb
def bubble(a):
    y = len(a)
    count = 0

    while count < y:
        DidweSwap = False
        for num in range(y - 1):
        # pdb.set_trace()
            if (num != (y - 1)) and (a[num] > a[num + 1]):
                swap(a,num)
                DidweSwap = True
        count = count + 1
        if DidweSwap == False:
            break
        print(*a)

def swap(a, num):
    temp = 0
    temp = a[num + 1]
    a[num + 1] = a[num]
    a[num] = temp
    return a

a = [1,2,3,4]
bubble(a);

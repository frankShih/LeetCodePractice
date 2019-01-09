def twoTrackOrder(arr):
    length = len(arr)
    rangeChecker = length//2 if length%2==0 else length//2+1

    for i in range(1, length, 2):
        for j in range(1, rangeChecker):
            print(i, i+j)
            swap(i, i+j, arr)
        rangeChecker-=1
    
    print(arr)

def swap(i, j, arr):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp

array = [i for i in range(1, 7+1)]
print("origin", array)
print("bubble sort fashion. time: O(N^2), space:O(N^2)")
twoTrackOrder(array)


def twoTrackOrder2(arr):
    length = len(arr)
    rangeChecker = length//2 if length%2==0 else length//2+1
    start=1
    for i in range(rangeChecker, length):
        temp = arr[i]
        # print(arr[i], "start", start, i, "temp", temp)
        for j in range(i, start, -1):
            arr[j] = arr[j-1]
        arr[start]=temp
        start+=2
    
    print(arr)

array = [i for i in range(1, 8+1)]
print("insertion sort fashion. time: O(N^2), space:O(N)")
twoTrackOrder2(array)


def twoTrackOrder3(arr):
    length = len(arr)
    rangeChecker = length//2 if length%2==0 else length//2+1
    newArr = [0]*length
    ind1,ind2=0, 1
    for i in range(length):
        if i<rangeChecker:
            newArr[ind1]=arr[i]
            ind1+=2
        else:
            newArr[ind2]=arr[i]
            ind2+=2
        
    print(newArr)

array = [i for i in range(1, 8+1)]
print("space change time. time: O(N), space:O(N)")
twoTrackOrder3(array)
def countingSort(arr, exp1): 
    n = len(arr) 
    output = [0] * n
    count = [0] * 10 # (0-9)

    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = arr[i]//exp1
        count[ index%10 ] += 1

    # Change count[i] so that count[i] now contains actual 
    # position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 

    # Build the output array 
    for i in range(n-1, -1, -1): 
        index = arr[i]//exp1
        output[ count[ index%10 ] - 1] = arr[i] 
        count[ index%10 ] -= 1

    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,n): 
        arr[i] = output[i] 

def radixSort(arr): 
    max1 = max(arr) 

    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp) 
        exp *= 10

inputList = [19,2,31,45,6,11,121,27]
print(inputList)
radixSort(inputList) 
print(inputList)

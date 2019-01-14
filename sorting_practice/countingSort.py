# sort arr[] in alphabetical order 
def countSort(arr): 
    n = len(arr) 
    result = arr[:]
    # the indices which value 'i' should be palce at
    output = [0 for i in range(256)] 

    # store count of inidividul characters 
    count = [0 for i in range(256)] 

    for i in arr: 
        count[i] += 1

    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(256): 
        count[i] += count[i-1] 
    # print(count)
    # Build the output character array 
    for i in range(n): 
        output[count[arr[i]]-1] = arr[i] 
        count[arr[i]] -= 1

    for i in range(n): 
        result[i] = output[i]

    return result

inputList = [19,2,31,45,6,11,121,27]
print(inputList)
inputList = countSort(inputList) 
print(inputList)


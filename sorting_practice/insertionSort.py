
def insertion_sort(InputList):
    # from head to tail
    for i in range(1, len(InputList)):
        j = i
        curr = InputList[i]
    
        # move current element to sorted position (at left part of list)
        while (InputList[j-1] > curr) and (j >= 1):
            InputList[j] = InputList[j-1]
            j=j-1
        InputList[j] = curr


inputList = [19, 2, 31, 45, 6, 11, 121, 27]
insertion_sort(inputList)
print(inputList)
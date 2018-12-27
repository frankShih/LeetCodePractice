def swap(inputList, a, b):        
    inputList[a], inputList[b] = inputList[b], inputList[a] 


def bubblesort(inputList):

# Swap the elements to arrange in order
    for iter_num in range(len(inputList)-1,0,-1):
        for idx in range(iter_num):
            if inputList[idx]>inputList[idx+1]:
                swap(inputList, idx, idx+1)
                # temp = inputList[idx]
                # inputList[idx] = inputList[idx+1]
                # inputList[idx+1] = temp


inputList = [19,2,31,45,6,11,121,27]
bubblesort(inputList)
print(inputList)
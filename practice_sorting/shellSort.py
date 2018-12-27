
def shellSort(input_list):
    gap = len(input_list) // 2

    while gap > 0:
        print("gap size", gap)
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
        # Sort the sub list for this gap (insertion sort)
            while j >= gap and input_list[j - gap] > temp:
                print("insertion", j, j-gap)
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp
        
        print(input_list)
        # Reduce the gap for the next element
        gap = gap//2

inputList = [19, 2, 31, 45, 6, 11, 121, 27]
shellSort(inputList)
print(inputList)

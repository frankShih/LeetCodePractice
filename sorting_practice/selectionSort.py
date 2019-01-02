
def selection_sort(input_list):

    for idx in range(len(input_list)):
        # each round find the index of min value
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        
        # Swap it
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19, 2, 31, 45, 6, 11, 121, 27]
selection_sort(l)
print(l)
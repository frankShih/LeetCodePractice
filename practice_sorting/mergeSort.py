def merge_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

# Merge the sorted halves

def merge(left_half,right_half):
    res = []
    r, l = 0, 0
    while len(left_half) > l and len(right_half) > r:
        if left_half[l] < right_half[r]:
            res.append(left_half[l])
            l+=1
        else:
            res.append(right_half[r])
            r+=1
    
    if len(left_half) <= l:
        res = res + right_half[r:]
    else:
        res = res + left_half[l:]
    # print(len(left_half), len(right_half), left_half,right_half, res)
    return res

inputList = [19,2,31,45,6,11,121,27]
outputList = merge_sort(inputList)
print(inputList)
print(outputList)    
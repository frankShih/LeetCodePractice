
def binary_search(values, search_for, left, right):
    # found= False
    while left<right:
        mid=(left+right)//2
        if values[mid]>search_for:
            return binary_search(values, search_for, left, mid)
        elif values[mid]<search_for:   
            return binary_search(values, search_for, mid+1, right)
        else:
            # found=True
            print("found", search_for, "at:", mid)
            return True
    
    return False


    


l = [64, 34, 25, 12, 22, 11, 90]
l = sorted(l)
print(l)
print(binary_search(l, 11, 0, len(l)))
print(binary_search(l, 90, 0, len(l)))

def intpolsearch(values, x):
    left = 0
    right = (len(values) - 1)

    while left <= right and x >= values[left] and x <= values[right]:
        # Find the mid point （內插法，阿斯～
        mid = left + int(
            ((x - values[left])/(values[right] - values[left])) * float(right - left)
            )

        # Compare the value at mid point with search value 
        if values[mid] == x:
            return "Found "+str(x)+" at index "+str(mid)

        if values[mid] < x:
            left = mid + 1
    
    return "Searched element not in the list"


l = [64, 34, 25, 12, 22, 11, 90]
l = sorted(l)
print(l)
print(intpolsearch(l, 11))
print(intpolsearch(l, 90))
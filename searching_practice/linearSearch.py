
def linear_search(values, search_for):
    search_at = 0
    search_res = False

    # Match the value with each data element	
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            print("found", search_for, "at:", search_at)
            search_res = True
        else:
            search_at = search_at + 1

    if not search_res: 
        print(search_for, "not found")
    return search_res

l = [64, 34, 25, 12, 22, 11, 90]
print(l)
print(linear_search(l, 12))
print(linear_search(l, 91))
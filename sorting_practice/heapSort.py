# heapify subtree rooted at index i. n is heap size 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     
    r = 2 * i + 2     

    if l < n and arr[largest] < arr[l]: 
        largest = l 

    if r < n and arr[largest] < arr[r]: 
        largest = r 

    if largest != i: 
        # Change root (swap), and re-heapify
        arr[i],arr[largest] = arr[largest],arr[i] 
        heapify(arr, n, largest) 

def heapSort(arr): 
    n = len(arr) 

    # Build a maxheap (for first time). 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    
    # swap elements to the end, each round
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 


inputList = [19,2,31,45,6,11,121,27]
print(inputList)
heapSort(inputList) 
print(inputList)


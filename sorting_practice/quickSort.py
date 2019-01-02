
def swap(inputList, a, b):        
    inputList[a], inputList[b] = inputList[b], inputList[a] 

def myQuickSort(inputList, left, right):
        if left>=right: return
        pivot=inputList[left]
        i, j = left+1, right               
                
        while True:
            while i<=right:
                if pivot<inputList[i]:
                    break    
                i+=1                                
            while j>left:
                if pivot>inputList[j]:
                    break
                j-=1
                
            if i>=j: break
            swap(inputList, i, j)
        swap(inputList, left, j)    
        myQuickSort(inputList, left, j-1)
        myQuickSort(inputList, j+1, right)        
        

# if __name__ == "__main__":
    
inputList = [19,2,31,45,6,11,121,27]
myQuickSort(inputList, 0, len(inputList)-1)
print(inputList)       
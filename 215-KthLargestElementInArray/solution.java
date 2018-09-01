class Solution {
    public int findKthLargest(int[] nums, int k) {
        myHeapSort(nums);
        // System.out.println("result: ");    
        // for(int i: nums){
        //     System.out.print(i);    
        // }
        
        return nums[nums.length-k];
    }
    
    // 60%
    public void myHeapSort(int[] array) {
        // build maxHeap
        int currentLen=array.length;
        for(int i=(int)(Math.ceil(array.length/2))-1;i>=0; i--){
            myHeapify(array, i, currentLen);
            // for(int a: array){
            //     System.out.print(a);    
            // }
            // System.out.println();    
        }
        
        for(int i=array.length-1;i>0; i--){
            swap(0, i, array);
            myHeapify(array, 0, i);
        }
        
        
    }
    
    public void myHeapify(int[] array, int root, int len){  //maxHeap
        int leftChild=root*2+1;
        int rightChild=root*2+2;
        int maxNode=-1;
        
        if(leftChild<len && array[leftChild]>array[root]){
            maxNode=leftChild;
        } else{
            maxNode=root;
        }
        
        if(rightChild<len && array[rightChild]>array[maxNode]){
            maxNode=rightChild;
        }
        
        if(maxNode!=root){
            swap(maxNode, root, array);
            myHeapify(array, maxNode, len);
        }   
        
    }
    
    //90% 
    public void myQuickSelectPartition(int[] list, int left, int right, int pivotIndex){
        int pivotValue = list[pivotIndex];
        swap(pivotIndex, right, list);  // Move pivot to end
        int storeIndex = left;
        for(int i=left; i<right; i++){
            if(list[i] < pivotValue){
                swap(storeIndex, i, list);
                storeIndex++;   
                // sequentially put the value smaller than pivot to the left
            }
        }
        swap(storeIndex, right, list);
        // Move pivot to its final place
        return storeIndex
    }

    // part;y sorting, best: O(n); worst O(n^2), depends on random initializaiton 
    public void myQuickSelect(int[] list, int left, int right, int k){
        if (left == right) return list[left];
        Random rand = new Random();
        int pivotIndex = rand.nextInt(right - left + 1)+left;     
        // select a pivotIndex between left and right,
        
        pivotIndex = myQuickSelectPartition(list, left, right, pivotIndex)

        // The pivot is in its final sorted position
        if (k == pivotIndex){
            return list[k];
        } else if (k < pivotIndex){
            return myQuickSelectPartition(list, left, pivotIndex - 1, k);
        } else
            return myQuickSelectPartition(list, pivotIndex + 1, right, k);
    }
    
     

    public void swap(int i, int j, int[] array){
        int temp=array[i];
        array[i]=array[j];
        array[j]=temp;
    }
}

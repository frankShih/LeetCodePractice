class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        // 80%
        int counter=0, ind=0;
        
        while(ind<flowerbed.length){
            if(flowerbed[ind]==0 && (ind==0 || flowerbed[ind-1]==0) && (ind==flowerbed.length-1 || flowerbed[ind+1]==0)){
                counter=counter+1;
                flowerbed[ind]=1;
            }
            
            if(counter>=n){
                return true;
            }
            
            ind = ind+1;
        }
        
        return false;
    }
}
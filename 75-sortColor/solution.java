class Solution {
    public void sortColors(int[] nums) {
        // 100%
        int[] counter = {0, 0, 0};
        for(int i: nums){
            counter[i]++;
        }
        
        int ind=0;
        for(int i=0; i<counter.length; i++){
            int c = 0;
            while(c<counter[i]){
                c++;
                nums[ind] = i;
                ind++;
            }
        }
    }
}
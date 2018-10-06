class Solution {
    public int singleNonDuplicate(int[] nums) {
        // 100%
        int l=0, r=nums.length-1;
        int m=-1;
        while(l<r){
            m=l+(r-l)/2;
            if(m%2==1) m-=1;   // for simplicity
            
            if(nums[m]==nums[m+1]){
                l=m+2;
            }else{
                r=m;
            }
        }
        return nums[l];
    }
}
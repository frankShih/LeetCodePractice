class Solution {
    // 100%
    public int[] searchRange(int[] nums, int target) {
        int start = binarySearch(nums, target);        
        int end = binarySearch(nums, target+1)-1;
        if(start==nums.length || nums[start]!=target){
            // empty array & target not found
            return new int[]{-1, -1};
        } else {
            return new int[]{start, Math.max(start, end)};
        }
         

    }
    
    private int binarySearch(int[] nums, int target) {
        int l=0, r=nums.length, m=-1;   
        // set right to array length for searching "target+1" offset (-1)
        while(l<r) {
            m=l+(r-l)/2;
            if(nums[m]<target){
                l=m+1;
            }else{
                r=m;
            }
        }
        return l;
    }
}
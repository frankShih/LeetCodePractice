1
class Solution {
    public boolean checkPossibility(int[] nums) {
        
        // 40%
        boolean flag = false;
        int p = -1;     //the position that break the rule
        
        for(int i=0; i<nums.length-1; i++){
            if(nums[i]>nums[i+1]){
                if(flag) return false;
                p=i;
                flag=true;
            }                            
        }
        
        return (!flag || p==0 || p==nums.length-2 || nums[p-1]<=nums[p+1] || nums[p]<=nums[p+2]);
    }
}
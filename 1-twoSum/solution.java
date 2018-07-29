// 90%
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> numPos = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length ; i++) {
            Integer position = numPos.get(target-nums[i]);
            if(position == null) {
                numPos.put(nums[i],i);
            } else {
                return new int[]{ i, position };
            }
        }
        return null;
    }
}

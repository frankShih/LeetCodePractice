class Solution {
    public int[] twoSum(int[] numbers, int target) {

        // 30%
        Map<Integer, Integer> map = new HashMap();
        
        for(int i=0; i<numbers.length; i++){
            if(map.containsKey(numbers[i])){
                return new int[] {map.get(numbers[i])+1, i+1};
                
            }else{
                map.put(target-numbers[i], i);
            }
        }
        
        return new int[] {};


        // 100%
        int head=0, tail=numbers.length-1;
        while(head<tail){
            if((numbers[head]+numbers[tail])>target){
                tail = tail-1;
            }else if((numbers[head]+numbers[tail])<target){
                head = head+1;
            }else{
                return new int[] {head+1, tail+1};
            }
        }

        return new int[] {};



    }
}

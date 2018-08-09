class Solution {
    public List<Integer> partitionLabels(String S) {
        List<Integer> result = new ArrayList();

        // 20%
        Map<Character, Integer> map = new HashMap();
        
        for(int i=0; i<S.length(); i++){
            map.put(S.charAt(i), i);            
        }
        
        int head=-1, tail=0;
        for(int i=0; i<S.length(); i++){
            tail = Math.max(map.get(S.charAt(i)), tail);
            if(tail==i){
                result.add(tail-head);
                head=tail;    
            }
        }
        

        // 92%                
        int[] map = new int[26];
        
        for(int i=0; i<S.length(); i++){
            map[S.charAt(i)-'a']=i;            
        }
        
        int head=-1, tail=0;
        for(int i=0; i<S.length(); i++){
            tail = Math.max(map[S.charAt(i)-'a'], tail);
            if(tail==i){
                result.add(tail-head);
                head=tail;    
            }
        }


        return result;
        
    }
}
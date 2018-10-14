class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> result= new ArrayList<>();
        
        // 50%
        for(int i=0;i<input.length(); i++){
            char c = input.charAt(i);
            if(!Character.isDigit(c)){
                List<Integer> left=diffWaysToCompute(input.substring(0, i));
                List<Integer> right=diffWaysToCompute(input.substring(i+1));
                
                for(int l: left){
                    for(int r: right){
                        switch(c){
                            case '+':
                                result.add(l+r);
                                break;
                            case '-':
                                result.add(l-r);
                                break;
                            case '*':
                                result.add(l*r);
                                break;
                            default:
                                result.add(l%r);
                        }
                    }
                }
            }
        }
        
        if(result.size()==0){
            result.add(Integer.valueOf(input));
        }
        
        return result;
    }
}
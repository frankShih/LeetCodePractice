class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        // 70%    
        /*
        for(char c : letters){
            if(c-target >0){
                return c;
            }
        }
        
        return letters[0];
        */
        
        // 40%
        int l=0, r=letters.length-1, m=-1;
        
        while(l<=r){
            m=l+(r-l)/2;
            if(letters[m]-target<=0){
                l=m+1;
            }else{
                r=m-1;
            }
        }
        
        return l<letters.length? letters[l]: letters[0];
    }
}
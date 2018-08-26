class Solution {
    public String findLongestWord(String s, List<String> d) {
        // 40%
        int best=-1;
        String best_word="";        
        int s_len=s.length();
        // 70% avoid memory re-allocation
        int ind1, ind2, w_len;


        for(String word : d){            
            ind1=0; 
            ind2=0;
            
            while(ind1<s_len){
                w_len=word.length();
                if(s_len-ind1<w_len-ind2)   break;
                
                if(s.charAt(ind1)==word.charAt(ind2)) ind2++;
                
                ind1++;                                    
                
                if(ind2==w_len){
                    if(ind2>best || ind2==best && best_word.compareTo(word)>0){
                        best=ind2;
                        best_word=word;
                    }   
                    break;
                }
            }
        }
        
        return best_word;
    }
}
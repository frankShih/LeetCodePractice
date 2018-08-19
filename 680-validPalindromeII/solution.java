class Solution {
    public boolean validPalindrome(String s) {
        return isPalindrome(s, 0);    
    }
    
    // 60%
    public boolean isPalindrome(String s, int falseCount) {
        int start=0, end=s.length()-1;
        
        if (falseCount>1)   return false;

        while(start<end){
            if (s.charAt(start)==s.charAt(end)){
                start++;
                end--;

            } else {
                // System.out.println(s.substring(start, end)+" : "+s.substring(start+1, end+1));
                return isPalindrome(s.substring(start, end), falseCount+1) || isPalindrome(s.substring(start+1, end+1), falseCount+1);
            }
        }

        return true;

    }

}
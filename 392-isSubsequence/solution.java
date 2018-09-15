public class Solution {
    public boolean isSubsequence(String s, String t) {
        // 30%
        if (s.length() == 0) return true;
        int indexS = 0, indexT = 0;
        while (indexT < t.length()) {
            if (t.charAt(indexT) == s.charAt(indexS)) {
                indexS++;
                if (indexS == s.length()) return true;
            }
            indexT++;
        }
        return false;
        
/*      
        // 90%
        if(t.length() < s.length()) return false;
        int prev = 0;
        for(int i = 0; i < s.length();i++)
        {
            char tempChar = s.charAt(i);
            prev = t.indexOf(tempChar,prev);    //char, fromIndex
            if(prev == -1) return false;
            prev++;
        }
        
        return true;
*/
    }
}
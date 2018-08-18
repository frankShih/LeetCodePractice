public class Solution {
    public String reverseVowels(String s) {
        // 54%
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        char[] chars = s.toCharArray();
        
        int l = 0, r = chars.length-1;
        while (l < r) {
            while (l < r && !vowels.contains(chars[l])) {
                l++;
            }
            while (l < r && !vowels.contains(chars[r])) {
                r--;
            }
            char tmp = chars[l];
            chars[l++] = chars[r];
            chars[r--] = tmp;
        }
        return new String(chars);
        

        // 10%
        Stack<Character> st = new Stack<Character>();
        char[] chars = s.toCharArray();
        for (char c : chars){
            if (vowels.contains(Character.toLowerCase(c))){
                st.push(c);
            }
        }
        
        for (int i=0; i< chars.length; i++){
            if (vowels.contains(Character.toLowerCase(chars[i]))){
                chars[i] = st.pop();
            }
        }

        return new String(chars);
    }
}
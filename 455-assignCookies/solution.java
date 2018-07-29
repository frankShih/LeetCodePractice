public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        //80%
        Arrays.sort(g);
        Arrays.sort(s);
        
        int ind1 = 0; 
        int ind2 = 0; 
        
        while(ind1<g.length && ind2<s.length){
            if(s[ind2]>=g[ind1]){
                ind1++;
            }
            ind2++;
        }
        return ind1;
    }
}
class Solution {
    public int mySqrt(int x) {
        
        // 90%
        // return (int)Math.sqrt(x);
        
        // 90%
        int l=1, h=x;
        int m, sqrt;
        while(l<=h){
            m = l + (h-l)/2;
            sqrt = x/m;
            // System.out.println("sqrt:"+sqrt);
            if(sqrt==m){
                // System.out.println(1);
                return m;
            }else if(sqrt>m){
                // System.out.println(2);
                l=m+1;
            }else{
                // System.out.println(3);
                h=m-1;
            }
        }
        return h;
    }
}
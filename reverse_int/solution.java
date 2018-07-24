class Solution {
    public int reverse(int x) {
        int result = 0;
        
        // 10%
        boolean sign = x>0;
        x = sign? x: x*-1;
                    
        while(x>0){                        
            if(result>Integer.MAX_VALUE/10 || result<Integer.MIN_VALUE/10){
                return 0;
            }
            result = result*10 + x%10;            
            x /= 10;            
            
        }
        
        return sign? result: -1*result;   
        
        
        /*
        // 5%
        int offset = x>0? 0:1;
        char temp = ' ';
        char[] c = String.valueOf(x).toCharArray();
        // System.out.println(Integer.MAX_VALUE+" : "+Integer.MIN_VALUE);
        for(int ind=0+offset;ind<c.length/2+offset;ind++){
            System.out.println(ind);
            temp = c[ind];
            c[ind] = c[c.length-ind-1+offset];
            c[c.length-ind-1+offset] = temp;
        }
        
        if(Long.parseLong(String.valueOf(c))>Long.parseLong(
            String.valueOf(Integer.MAX_VALUE)) || Long.parseLong(String.valueOf(c))<Long.parseLong(
            String.valueOf(Integer.MIN_VALUE))){
            return 0;
        } else{
            return Integer.parseInt(String.valueOf(c)); 
        }
        */

        /*
        // 90%
        //*
        the operation of '/' and '%' in java is different from python
        e.g. 51/10 = 5, -51/10=-5, 51%10=1, -51%10=-1
         */
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
        */
    }      
}
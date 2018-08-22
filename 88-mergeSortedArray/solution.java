public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        /*
        // 5%
        //int p = m+n, p1 = m-1, p2 = n-1;
        while(m+n-1>=0) {
            if(m-1<0 || (n>0 && nums1[m-1]<nums2[n-1])){
                nums1[m+n-1] = nums2[n-1];
                n--;
            } 
            else{
                nums1[m+n-1] = nums1[m-1];
                m--;
            } 
        }
        */
        
        // 25%
        while(n>0){
            if(m>0&&nums1[m-1]>nums2[n-1]){
                nums1[m+n-1] = nums1[m-1];
                m--;
            }
            else{
                nums1[m+n-1] = nums2[n-1];
                n--;
            }
        }
    }
}
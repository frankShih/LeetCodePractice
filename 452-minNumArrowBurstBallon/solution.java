class Solution {
    public int findMinArrowShots(int[][] points) {

        // 4%
        Arrays.sort(points, (a, b) -> 
                    (a[0] == b[0] ? /*b.start - a.start*/1 : b[0]-a[0] ));
        // sorted by end (ascend)
        long start = Long.MAX_VALUE;
        int count = 0;
        for (int i = 0; i < points.length; i++) {
            if (points[i][1] < start){
                start = points[i][0];
                count++;
            }             
        }
        return count;


        // 10%
        if(points.length<2) return points.length

        Arrays.sort(points, (a, b) -> (b[0]-a[0]));
        // sorted by end (ascend)
        int start = points[0][0];
        int count = 1;
        for (int i = 1; i < points.length; i++) {
            if (points[i][1] < start){
                start = points[i][0];
                count++;
            }             
        }
        return count;

    }
}
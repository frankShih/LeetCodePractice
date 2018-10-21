class Solution {
    /*
    // 67%
    public int numSquares(int n) {
        List<Integer> squares = generateSquares(n);
        Queue<Integer> queue = new LinkedList<>();
        boolean[] marked = new boolean[n + 1];
        queue.add(n);
        marked[n] = true;
        int level = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            level++;
            while (size-- > 0) {
                int cur = queue.poll();
                for (int s : squares) {
                    int next = cur - s;
                    if (next < 0) {
                        break;
                    }
                    if (next == 0) {
                        return level;
                    }
                    if (marked[next]) { // have been checked before, don't queue again
                        continue;
                    }
                    marked[next] = true;
                    queue.add(next);
                }
            }
        }
        return n;
    }

   // mathematical rule to generate square sequence
    private List<Integer> generateSquares(int n) {
        List<Integer> squares = new ArrayList<>();
        int square = 1;
        int diff = 3;
        while (square <= n) {
            squares.add(square);
            square += diff;
            diff += 2;
        }
        return squares;
    }
    */
// 90%
    public int numSquares(int n) {
        int[] memory = new int[n + 1];        
        for(int i=1; i<=n; i++){
            int candidate = Integer.MAX_VALUE;
            
            for(int j=1; j*j<=i; j++){
                candidate = Math.min(candidate, memory[i-j*j]+1);
            }
            memory[i] = candidate;
        }
        
        return memory[n];
    }
}
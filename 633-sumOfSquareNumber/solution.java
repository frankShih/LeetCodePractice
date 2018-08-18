 public boolean judgeSquareSum(int c) {
     /*
    //  15%
        for (long a = 0; a * a <= c; a++) {
            int b = c - (int)(a * a);
            if (binary_search(0, b, b))
                return true;
        }
        return false;
        */

        // 30%
        for (int a = 0; a <= Math.sqrt(c)+1; a++) {
            double b = Math.sqrt(c - (a * a));
            if ((b == Math.floor(b)) && !Double.isInfinite(b)) return true;
        }
        return false;
    }

    
    public boolean binary_search(long s, long e, int n) {
        if (s > e)
            return false;
        long mid = s + (e - s) / 2;
        if (mid * mid == n)
            return true;
        if (mid * mid > n)
            return binary_search(s, mid - 1, n);
        return binary_search(mid + 1, e, n);
    }
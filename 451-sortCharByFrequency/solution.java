class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();  // create freq count map
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        
        // 40%
        List<Character> [] bucket = new List[s.length() + 1];   // turn map to order list
        for (char key : map.keySet()) {
            int frequency = map.get(key);
            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(key);
        }
        
        StringBuilder sb = new StringBuilder();     //turn list to string
        for (int pos = bucket.length - 1; pos >=0; pos--) {
            if (bucket[pos] != null) {
                for (char key : bucket[pos]) {
                    for (int i = 0; i < map.get(key); i++) {
                        sb.append(key);
                    }
                }
            }
        }
        /*
        // 30%
        PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(
            new Comparator<Map.Entry<Character, Integer>>() {
                @Override
                public int compare(Map.Entry<Character, Integer> a, Map.Entry<Character, Integer> b) {
                    return b.getValue() - a.getValue();
                }
            }
        );
        pq.addAll(map.entrySet());
        
        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            Map.Entry e = pq.poll();
            for (int i = 0; i < (int)e.getValue(); i++) {
                sb.append(e.getKey());
            }
        }
        */
        return sb.toString();
        
    }
}
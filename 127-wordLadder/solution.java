class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        /*
        // 92% least-nodes-first bi-directional BFS
        Set<String> dict = new HashSet<>(wordList);
        Set<String> startQ = new HashSet<>();
        Set<String> endQ = new HashSet<>();
        Set<String> visited = new HashSet<>();
        
        if(!dict.contains(endWord)){
            return 0;
        }
        
        startQ.add(beginWord);
        endQ.add(endWord);
        
        for(int leng = 2;!startQ.isEmpty();leng++){
            Set<String> neighbours = new HashSet<>();
            
            //go through all the nodes in the queue
            for(String node: startQ){                
                //for each node, visit their neighbouring nodes
                for(int i=0;i<node.length();i++){
                    StringBuilder transformWord = new StringBuilder(node);
                    char exclude = transformWord.charAt(i);
                    for(char c='a';c<='z';c++){
                        if(c == exclude){
                            continue;
                        }
                        transformWord.setCharAt(i,c);
                        String tWord = transformWord.toString();

                        if(endQ.contains(tWord)){
                            return leng;
                        }

                        if(dict.contains(tWord) && visited.add(tWord)){
                            neighbours.add(tWord);
                        }
                    }
                }
            }
            
            //by here, we have processed all of previous queue
            //Choose the shortest between the startQ and endQ
            //in hopes to alternate between them to meet somewhere
            //at the middle. This optimizes the code, because we are processing 
            //smallest queue first, so # of nodes dont blow up as fast.
            //basically balancing between the two queues
            startQ = (neighbours.size() > endQ.size()) ? endQ : neighbours;
            endQ = (startQ == neighbours) ? endQ : neighbours;
        }
        
        return 0;
        */

        // 45% BFS
        List<String> taskQ = new ArrayList();
        taskQ.add(beginWord);
        Map<String, Integer> dict = new HashMap<String, Integer>();
        for(String s: wordList){
            dict.put(s, 0);
        }
        int path =1;

        while(taskQ.size()>0){

            int size=taskQ.size();
            List<String> neighbours = new ArrayList();
            while(size>0){

                size--;
                String word = taskQ.remove(0);
                // System.out.println("1 inin "+word);

                for(int i=0; i<word.length(); i++){
                    StringBuilder transformWord = new StringBuilder(word);

                    for(char alphabet = 'a'; alphabet <='z'; alphabet++ ){
                        transformWord.setCharAt(i,alphabet);
                        String tWord = transformWord.toString();
                        
                        
                        if (dict.get(tWord)==null || dict.get(tWord)==1){
                            continue;
                        }
                        if (tWord.equals(endWord)){
                            return path+1;
                        }
                        neighbours.add(tWord);
                        dict.put(tWord, 1);
                    }
                }
            }
            for(String s: neighbours) {
                // System.out.print(s+", ");
                taskQ.add(s);
            }
            // System.out.println(" ");
            path+=1;
        }
        return 0;
    }
}
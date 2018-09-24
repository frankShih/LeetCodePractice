public class Solution {
    public int maxProfit(int[] prices) {
        /*
        int currMin=prices.length==0 ? 0: prices[0];
        int profit=0, temp=0;
        
        for(int i=1; i<prices.length; i++){
            if(currMin>prices[i])   currMin=prices[i];
            if(prices[i]-currMin>temp){
                temp = prices[i]-currMin;
                if(i==prices.length-1) profit+=temp;
            }else{
                profit+=temp;
                temp=0;
                currMin = prices[i];
            }
        }
        
        return profit;
        */
        int total = 0;
        for (int i=0; i< prices.length-1; i++) {
            if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
        }
        
        return total;
    }
}
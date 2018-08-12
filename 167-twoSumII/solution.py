class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 85%
        d={};
        for i in range(len(numbers)):
            if target-numbers[i] in d:
                print numbers[i]
                return [d[target-numbers[i]]+1, i+1]
            else:
                d[numbers[i]] = i
        return []        


        head, tail = 0, len(numbers)


        # 25%
        head, tail = 0, len(numbers)-1
        
        while head<tail:
            if (numbers[tail]+numbers[head])>target:
                tail-=1
            elif (numbers[tail]+numbers[head])==target:
                return [head+1, tail+1]
            else:
                head+=1
                
        return []
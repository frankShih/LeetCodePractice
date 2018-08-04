class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # 99%
        people=sorted(people ,key=lambda l:(l[0], -l[1]), reverse=True)        
        length = len(people)                

        if len(people)<2:   return people

        result = [people[0]]
        for i in range(1, length):            
            # print(result)
            result.insert(people[i][1], people[i])
                                    
        return result
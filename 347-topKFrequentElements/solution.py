class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 50%
        result = []
        dic = dict()
        
        for n in nums:
            if not(n in dic):
                dic[n]=1
            else:
                dic[n]+=1
        
        inv_dic = {}
        for key, val in dic.items():
            if not(val in inv_dic):
                inv_dic[val]=[key]
            else:
                inv_dic[val].append(key)
        # for k, v in inv_dic.items():
        #     print(k, v)
        
        counter=0
        for i in range(len(nums), -1, -1):
            if i in inv_dic:
                # print(inv_dic[i], i, len(inv_dic[i]))
                counter+=len(inv_dic[i])
                result.extend(inv_dic[i])
            # print(counter)
            if counter==k:
                # print(counter, k)
                break

        return result        


        '''
        # oneline solution
        from collections import Counter
        return [key for key, count in Counter(nums).most_common(k)]
        '''

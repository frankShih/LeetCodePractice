class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 70%
        dic = {}
        for c in s:
            if not(c in dic):
                dic[c]=1
            else:
                dic[c]+=1
        kk, vv = list(dic.keys()), list(dic.values())
        # print(kk, vv)
        ind = sorted(range(len(kk)), key=lambda k: vv[k], reverse=True)        
        # print(ind)
        temp=[]
        for i in ind:
            temp.extend([kk[i]]*vv[i])
            
        # print(temp)
        return ''.join(temp)

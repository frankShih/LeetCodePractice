class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        result=[]

        if not s:
            return result

        def isPalindrome(ss):
            start, end = 0, len(ss)-1

            while start<end:
                if ss[start]==ss[end]:
                    start+=1
                    end-=1
                else:
                    return False

            return True

        taskQ = [[0, []]]
        length = len(s)

        # BFS, 38%
        while taskQ:
            ind, com = taskQ.pop(0)
            # print(ind, com)
            if ind==length:
                result.append(com)
            
            for j in range(1, length+1):
                if ind+j > length:
                    break
                if isPalindrome(s[ind:ind+j]):
                    # print(ind, j, s[ind:ind+j])
                    taskQ.append([ind+j, com+[s[ind:ind+j]]])

        return result



        

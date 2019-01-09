class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
            
        wordSet = set(wordDict)
        # naive BFS, O(M^N)
        Q = [[s, []]]
        result = []
        while Q:
            remain, path = Q.pop(0)

            if not remain:
                result.append(" ".join(path))
                continue

            for w in wordDict:
                if remain.startswith(w):
                    Q.append([remain[len(w):], path+[w]])
            # length = len(remain)
            # for i in range(length+1):
            #     if remain[:i] in wordSet:
            #         Q.append([remain[i:], path+[remain[:i]]])


        return result



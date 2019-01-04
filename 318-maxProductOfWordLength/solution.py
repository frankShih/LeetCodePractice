class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 25%
        if not words:
            return 0
        
        length = len(words)
        best = 0
        letters=[set(w) for w in words]
        lengths=[len(w) for w in words]
        

        for i in range(length):
            for j in range(i+1, length):
                if not (letters[i] & letters[j]):
                    temp = lengths[i]*lengths[j]
                    best = temp if temp>best else best

        return best
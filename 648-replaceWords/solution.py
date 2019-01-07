class Solution:
    def replaceWords(self, dic, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # wordBank = set(dic)
        words = sentence.split(' ')
        # print(words)

        for i in range(len(words)) :
            for s in dic:
                if words[i].startswith(s):
                    words[i] =s

        # print(words)

        return ' '.join(words)
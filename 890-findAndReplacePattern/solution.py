class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []

        if not words or not pattern:
            return result

        pLen = len(pattern)
        mapping = {}
        revMapping = {}

        for word in words:
            wLen = len(word)
            if wLen!=pLen:
                continue

            mapping.clear()
            revMapping.clear()

            for i in range(wLen):
                if pattern[i] not in mapping:
                    if word[i] in revMapping:
                        # diff patterns map to same value
                        break
                    
                    mapping[pattern[i]] = word[i]
                    revMapping[word[i]] = pattern[i]
                elif mapping[pattern[i]] != word[i]:
                    # same pattern map to diff values   
                    break
                
                if i==wLen-1:
                    result.append(word)

        return result
        
        '''
        # more consice way, change mapping from dict to list
        def compare(a, b):
            # Completely Same Idea of # 205. Isomorphic Strings
            if len(a) != len(b):
                return False
            # keep the mapping in array
            rec_a = [-1]*26  # map from indA to indB
            rec_b = [-1]*26
            for i in range(len(a)):
                ax = ord(a[i])-ord('a')
                bx = ord(b[i])-ord('a')

                if rec_a[ax] == rec_b[bx]:  # not mapping yet
                    rec_a[ax] = rec_b[bx] = i
                else:
                    return False
            return True

        return [w for w in words if compare(w, pattern)]
        '''

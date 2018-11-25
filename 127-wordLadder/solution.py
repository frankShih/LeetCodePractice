import string

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 30%, acceptable solution
       
        taskQ = [beginWord]
        word_list = {i: 0 for i in wordList}
        path = 1  
        
        while len(taskQ)>0:
            size = len(taskQ)
            
            candidates=[]
            
            while size>0:
                size-=1
                word = taskQ.pop(0)
                
                for i in range(len(word)):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        w = word[:i]+letter+word[i+1:]
                       
                        if word_list.get(w, -1)<0:
                            continue
                        if word_list[w]:
                            continue
                        
                        if w == endWord:
                            return path+1
                        candidates.append(w)
                        word_list[w]=1
                
            candidates = list(set(candidates))
            taskQ.extend(candidates)
                
            path+=1
        return 0
    '''
    # 80% using set (bigO(1) when checking exist) & bi-direction BFS
        word_dict =set(wordList)
        fQ = [beginWord]
        bQ = [endWord]
        fCount, bCount = 0, 1  
        fInd, bInd = 0, 0
        fRecord=set()
        bRecord=set()

        if not(endWord in word_dict): return 0
        while True:
            # first part ~~ 25%
            if len(fQ)<=len(bQ):
                candidates=[]

                for i in range(fInd, len(fQ)):
                    word = fQ[i]
                    
                    for i in range(len(word)):
                        for letter in 'abcdefghijklmnopqrstuvwxyz':
                            w = word[:i]+letter+word[i+1:]
                            if not(w in word_dict): continue
                            if w in fRecord: continue
                            
                            candidates.append(w)
                            fRecord.add(w)

                candidates = list(set(candidates))
                if len(candidates)==0: break
                fInd=len(fQ)
                fQ.extend(candidates)
                fCount+=1
                if set(fQ) & set(bQ):
                    return fCount+bCount
            else:
                candidates=[]

                for i in range(bInd, len(bQ)):
                    word = bQ[i]
                    
                    for i in range(len(word)):
                        for letter in 'abcdefghijklmnopqrstuvwxyz':
                            w = word[:i]+letter+word[i+1:]
                            if not(w in word_dict): continue
                            if w in bRecord: continue
                            
                            candidates.append(w)
                            bRecord.add(w)
    
                candidates = list(set(candidates))
                if len(candidates)==0: break
                bInd=len(bQ)
                bQ.extend(candidates)
                bCount+=1
                if set(fQ) & set(bQ):
                    return fCount+bCount
            
        return 0
    '''

    '''
    # 90%, bi-direction BFS with less nodes
    word_dict = set(wordList)
        startQ = set()
        endQ = set()
        visited = set()
        
        if endWord not in word_dict:
            return 0
        
        startQ.add(beginWord)
        endQ.add(endWord)
        leng = 2
        while len(startQ) != 0:
            neighbours = set()
            for node in startQ:
                for i in range(0,len(node)):
                    char_arr = list(node)
                    exclude = ord(node[i]);
                    for j in range(ord('a'),ord('z')+1):
                        if j == exclude:
                            continue
                        
                        char_arr[i] = chr(j)
                        transformWord = ''.join(char_arr)
                        
                        if transformWord in endQ:
                            return leng
                        
                        if transformWord in word_dict and transformWord not in visited:
                            visited.add(transformWord)
                            neighbours.add(transformWord)
            
            startQ = endQ if len(endQ) < len(neighbours) else neighbours
            endQ = endQ if startQ == neighbours else neighbours
            leng += 1
        
        return 0
        '''   
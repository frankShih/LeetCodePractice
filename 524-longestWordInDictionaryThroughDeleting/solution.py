class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        # 30%        
        best=-1
        best_word=''

        # 75%   replace repetitive function call with variables !!!
        s_len=len(s)        

        for word in d:
            ind1, ind2 = 0, 0
            
            while ind1<s_len:
                w_len=len(word)

                # 40%       early stopping~~~
                if s_len-ind1 <w_len-ind2: break
                # print(word+" : "+str(ind1)+" : "+str(ind2)    )
                if s[ind1] == word[ind2]:
                    ind1+=1
                    ind2+=1
                else:
                    ind1+=1
                
                if ind2 == w_len:
                    if ind2 > best or ind2 == best and best_word>word:
                        best=ind2
                        best_word=word
                    break    
            
        return best_word
        
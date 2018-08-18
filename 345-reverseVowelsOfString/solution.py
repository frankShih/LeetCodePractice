class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 30% O(n) for indexing
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # 80%             important!!!   O(1) for indexing
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        indice = []
        for i in range(len(s)):
            if s[i] in vowels:
                indice.append(i)
        ls = list(s)
        for j in range(int(len(indice)/2)):
            temp = ls[indice[j]]
            
            ls[indice[j]] = ls[indice[-j-1]]
            ls[indice[-j-1]] = temp
            
        return "".join(ls)


        # 10%
        st=[]
        ls = list(s)
        for i in range(len(ls)):
            if ls[i] in vowels:
                st.append(ls[i])
        
        for i in range(len(ls)):
            if ls[i] in vowels:
                ls[i] = st.pop()
        
        
        return "".join(ls)




from itertools import cycle

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # length = len(letters)
        # cycled = cycle(letters)        
        # counter = 1
        '''
        # 15%
        while True:
            temp = next(cycled)
            if ord(temp)>ord(target):
                return temp                    
            
            if counter>length:
                return temp
            
            counter += 1
        '''    
            
        alphabets = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
        '''
        # 25%
        while True:
            temp = next(cycled)
            if alphabets[temp]>alphabets[target]:
                return temp                    
            
            if counter>length:
                return temp
            
            counter += 1
        '''
        # 36%
        for temp in letters:
            if alphabets[temp]>alphabets[target]:
            # if ord(temp)>ord(target):
                return temp                    
            
        return letters[0]    
        
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        if not s:
            return counter

        length = len(s)

        '''
        # list out all candidates O(N^2), 37%
        result = []

        def checkPalindrom(s, left, right, result):
            while left >= 0 and right <= length-1:
                if s[left] == s[right]:
                    result.append(s[left:right+1])
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(length):
            checkPalindrom(s, i, i, result)
            checkPalindrom(s, i, i+1, result)

        return len(result)
        '''

        # center-expanding checking maxLength of each palindrom O(N^2)
        def checkPalindrom(s, left, right):
            while left >= 0 and right <= length-1:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return right-left-1

        for i in range(length):
            temp = checkPalindrom(s, i, i)
            counter += (temp+1)//2
            if i < length-1 and s[i] == s[i+1]:
                temp = checkPalindrom(s, i, i+1)
                counter += (temp+1)//2

        return counter

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if not s:
            return result

        length = len(s)

        # if length < 2:
        #     return result

        records = []
        temp = s[0]
        counter = 1
        for i in range(1, length):
            if s[i] == temp:
                counter += 1
            else:
                records.append(counter)
                counter = 1
                temp = s[i]

        records.append(counter)
        # print(records)

        for i in range(1, len(records)):
            result += min(records[i-1], records[i])

        return result

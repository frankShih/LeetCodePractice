class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        result = []
        if not(s): return result

        length = len(s)
        '''
        # naive solution, 90%
        candidates=[]

        for i in range(1, 4):
            if i>=length or int(s[0:i])>255 or s[0]=='0' and i>1:
                continue

            for j in range(1, 4):
                if  i+j>=length or int(s[i:i+j])>255 or s[i]=='0' and j>1:
                    continue
                
                for k in range(1, 4):
                    if  i+j+k>=length or int(s[i+j:i+j+k])>255 or s[i+j]=='0' and k>1:
                        continue

                    if int(s[i+j+k:])>255 or s[i+j+k]=='0' and length-i-j-k>1:
                        continue
                    
                    candidates.append([i, i+j, i+j+k])

        for c in candidates:
            # print(s[:c[0]], s[c[0]:c[1]], s[c[1]:c[2]], s[c[2]:])
            result.append("{}.{}.{}.{}".format(s[:c[0]], s[c[0]:c[1]], s[c[1]:c[2]], s[c[2]:]))

        return result
        '''

        def go(current, leftover):
            if len(current) == 4:
                if len(leftover) == 0: 
                    result.append(current)
                return
            for i in range(1, min(4, len(leftover)+1)):
                prefix, new_leftover = leftover[-i:], leftover[:-i]
                if int(prefix) > 255: continue
                if prefix[0] == "0" and len(prefix) > 1: continue
                go([prefix] + current, new_leftover)
        
        go([], s)
        return [".".join(ip) for ip in result]

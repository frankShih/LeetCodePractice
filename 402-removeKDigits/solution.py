class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        '''
        # 20%
        if k>=len(num): return "0"
        
        stack1 = list(num)
        stack2 = []
        
        while stack1:
            stack2.append(stack1.pop(0)) 
            
            if stack1:
                if stack2[-1]>stack1[0] and k>0:
                    stack2.pop()
                    k-=1
                    if stack2:
                        stack1.insert(0, stack2.pop()) 
          

        leading = 0
        while leading<len(stack2)-1 and stack2[leading]=="0" : leading+=1
        stack2 = stack2[leading:len(stack2)-k]
        
        return "".join(stack2)
        '''

        # 50%
        stack = []
        for n in num:
            while stack and k>0 and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)

        leading = 0
        while leading<len(stack) and stack[leading] =='0':
            leading+=1

        return ''.join(stack[leading:len(stack)-k]) if leading<len(stack)-k else "0"   
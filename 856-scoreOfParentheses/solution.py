class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # naive Solution using stack O(N)
        stack = []

        for char in S:
            if char != ')':
                stack.append(char)
            else:
                temp = 0
                while stack[-1]!='(':
                    temp += stack.pop()    
                stack.pop()    
                # retrieve all content in a pair of parenthese to parse
                if not temp:
                    stack.append(1)
                else:
                    stack.append(temp*2)

        # print(stack)
        return sum(stack)
        '''

        # more concise solution O(N)
        stack = [0] # initialization
        for s in S:
            # print(stack, s)
            if s == '(':    # depth +1
                stack.append(0)
            else:   # ")" pop out & evaluate
                v = stack.pop()
                stack[-1]+=max(2*v, 1)

        return stack[0]
        '''

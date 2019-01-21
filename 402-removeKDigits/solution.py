class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        '''
        if k>=len(num):
            return "0"

        # two-pass greedy solution O(N) 18%
        stack1 = list(num)
        stack2 = []

        while stack1:
            stack2.append(stack1.pop(0))

            # non-increasing occurred
            if stack1 and stack2[-1]>stack1[0] and k>0:
                stack2.pop()
                k-=1
                if stack2:  # need to check previous values
                    stack1.insert(0, stack2.pop())

        # stack2 is now an increasing sequence
        remainLen, leading = len(stack2), 0
        while leading<remainLen-1 and stack2[leading]=="0":
            leading+=1

        return "".join(stack2[leading:remainLen-k])

        '''

        # using only one stack O(N), 89%
        stack = []
        for n in num:
            while stack and k>0 and stack[-1]>n:
                # non-increasing occurred
                stack.pop()
                k-=1

            stack.append(n)

        remainLen, leading = len(stack), 0
        while leading<remainLen and stack[leading] =='0':
            leading+=1

        return ''.join(stack[leading:remainLen-k]) if leading<remainLen-k else "0"

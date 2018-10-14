class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.traversal(self.parser(input))
        
    #    65%
    '''
        since using permutation have to deal with duplicate issue
        try another way of bottom-up approach
    '''
    def traversal(self, operation):
        # print(operation)
        result=[]
        
        if len(operation)==1:            
            return operation
        
        operator=set(['+', '-', '*', '/'])    
        
        for i in range(len(operation)):
            if operation[i] in operator:
                left=self.traversal(operation[:i])
                right=self.traversal(operation[i+1:])
                
                for operand1 in left:
                    for operand2 in right:
                        if operation[i]=='*':
                            result.append(operand1*operand2)
                        elif operation[i]=='+':
                            result.append(operand1+operand2)
                        elif operation[i]=='-':
                            result.append(operand1-operand2)
                        else:
                            result.append(operand1//operand2)                                                        
                
        return result
   
    def parser(self, chars):
        result=[]
        temp=""
        operator=set(['+', '-', '*', '/'])
        for c in chars:
            if not(c in operator):
                temp+=c
            else:
                result.append(temp)
                result.append(c)
                temp=""
                
        result.append(temp)
        if not(result[0].isnumeric()):
            result.insert(0, int(result[0]+result[1]))
            del result[1:3]
        return [int(x) if x.isnumeric() else x for x in result]
       
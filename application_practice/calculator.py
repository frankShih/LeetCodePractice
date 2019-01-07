class calculator:
    def __init__(self):
        print("calculator created")
        self.operator = ['+', '-', '*', '/']
        self.preserved = ['(', ')']

    def operate(self, operation):
        if len(operation)<3:
            return operation[0]

        op1, opt, op2 = operation
        if opt == "+":
            return op1+op2
        elif opt == "-":
            return op1-op2
        elif opt == "*":
            return op1*op2
        else:
            if op2 == 0:
                print("devide by zero, nan")
                return 0
            return op1/op2


    def calculate(self, operation):
        # print(operation)
        parsed = self.parse(operation)
        stack = []
        
        while parsed:   # deal with parentheses
            c = parsed.pop(0)
            if c == self.preserved[1]:
                subOperation = []
                temp = None
                while temp!=self.preserved[0]:
                    temp = stack.pop()
                    subOperation.insert(0, temp) 
                # print(subOperation)
                stack.append(self.operate(subOperation[1:]))
            else:
                stack.append(c)
        
        # print(stack)
        parsed, stack = stack, []

        while parsed:   # deal with multiply & devision
            c = parsed.pop(0)
            
            if c =='*' or c=='/':
                subOperation = []
                subOperation.append(stack.pop())
                subOperation.append(c)
                subOperation.append(parsed.pop(0))
                stack.append(self.operate(subOperation))

            else:
                stack.append(c)

        # print(stack)
        parsed = stack
        subOperation = []

        while parsed:   # deal with plus & minus
            subOperation.append(parsed.pop(0)) 
            
            if len(subOperation)==3:
                # print(subOperation)
                subOperation = [self.operate(subOperation)]
                # print(subOperation)

        print("the answer is:", subOperation)



    def parse(self, operation):
        stack = []
        temp = ''
        for c in operation:
            if c in self.preserved + self.operator:
                if temp:    
                    stack.append(float(temp))
                    temp = ''
                stack.append(c)
            else:   # is numeric
                temp+=c    
        if temp:    
            stack.append(float(temp))

        # print(stack)
        ind = len(stack)-1
        while ind >=0:
            if stack[ind]=='-' and (ind==0 or ind>0 and stack[ind-1]=='('):
                temp = float(stack[ind]+str(stack[ind+1]))
                del stack[ind:ind+2]
                stack.insert(ind, temp)
            ind-=1
        # print(stack)

        return stack


print(dir(calculator))
cc = calculator()
cc.calculate("-9/(-1+2)-3+(4*5)/6")
cc.calculate("-9*(-1+(-2))-3+(4*(-5))/2")


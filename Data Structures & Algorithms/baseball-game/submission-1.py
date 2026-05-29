class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            
            if ops == "+":
                arg_2,arg_1 = stack.pop(), stack.pop()
                _sum = arg_1+arg_2
                stack.append(arg_1)
                stack.append(arg_2)
                stack.append(_sum)
            
            elif ops == "C":
                stack.pop()
                
            elif ops == "D":
                arg_1 = stack.pop()
                stack.append(arg_1)
                stack.append(arg_1*2)

            else:
                stack.append(int(ops))
            print(ops)
            print(stack)
        return sum(stack)
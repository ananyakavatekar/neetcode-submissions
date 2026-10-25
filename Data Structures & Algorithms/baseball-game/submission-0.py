class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # when x seen just add 
        # pop and peek and add together when '+' is seen
        # peek top and *2 when 'D' is seen
        # pop when 'C' is seen
        stack = []

        for operation in operations:
            if (operation == '+'):
                stack.append(stack[len(stack) - 1] + stack[len(stack) - 2])
            elif (operation == 'D'):
                stack.append(stack[len(stack) - 1] * 2)
            elif (operation == 'C'):
                stack.remove(stack[len(stack) - 1]) 
            else: 
                stack.append(int(operation))
        
        stack_sum = 0
        for val in stack: 
            stack_sum += val
        
        return stack_sum

        
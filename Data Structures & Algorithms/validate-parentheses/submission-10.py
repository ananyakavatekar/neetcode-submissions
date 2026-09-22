class Solution:
    def isValid(self, s: str) -> bool:

        closing = {")" : "(", 
            "}" : "{", 
            "]" : "["}

        stack = [] # .append .pop lifo

        opening = {"[", "(", "{"}

        for bracket in s:
            if (bracket in closing and len(stack) == 0): 
                return False
            if bracket in opening: 
                stack.append(bracket)
            if bracket in closing: 
                if closing[bracket] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0



        
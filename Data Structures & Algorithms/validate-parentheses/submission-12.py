class Solution:
    def isValid(self, s: str) -> bool:


        closing = {")" : "(", "}": "{", "]" : "["}

        open_stack = []

        for i in range(len(s)):
            if (i == 0 and (s[i] in closing)):
                return False
            if (s[i] in closing):
                if (len(open_stack) > 0 and open_stack[-1] == closing[s[i]]):
                    open_stack.pop()
                else: 
                    return False
            else:
                open_stack.append(s[i])
        
        return len(open_stack) == 0
        

        
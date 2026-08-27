class Solution:
    def isValid(self, s: str) -> bool:
        # case where all brackets can't have an open and close
        if len(s) % 2 != 0:
            return False
        
        opening_lst = ["(", "[", "{"]
        closing_lst = [")", "]", "}"]

        corresponding = {")": "(", "}": "{", "]": "["}

        opening_stack = []
        
        for i in s: 
            if i in opening_lst:
                opening_stack += i
            if i in closing_lst:
                if len(opening_stack) > 0 and opening_stack[-1] == corresponding[i]:
                    opening_stack.pop()
                else:
                    return False
        
        return len(opening_stack) == 0 












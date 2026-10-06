class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        vals = []

        for item in tokens:
            if item == '+':
                vals.append(int(vals.pop()) + int(vals.pop()))
            elif item == '-':
                a, b = int(vals.pop()), int(vals.pop())
                vals.append(b - a)
            elif item == '*':
                vals.append(int(vals.pop()) * int(vals.pop()))
            elif item == '/':
                a, b = int(vals.pop()), int(vals.pop())
                vals.append(b/a)
            else: 
                vals.append(item)
    
        return int(vals.pop())

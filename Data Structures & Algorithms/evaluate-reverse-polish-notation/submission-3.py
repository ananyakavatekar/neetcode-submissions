class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        vals = []

        for item in tokens:
            if (item == '+'):
                vals.append(int(vals.pop()) + int(vals.pop()))
            elif (item == '-'):
                a, b = vals.pop(), vals.pop()
                vals.append(b - a)
            elif (item == '*'):
                vals.append(int(vals.pop()) * int(vals.pop()))
            elif (item == '/'):
                a, b = vals.pop(), vals.pop()
                vals.append(int(float(b) / a))
            else: 
                vals.append(int(item))
        
        return int(vals.pop())
            

            
                

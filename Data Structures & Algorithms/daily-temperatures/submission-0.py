class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        prev = temperatures[0]

        for i in range(len(temperatures)):
            curr = temperatures[i]
            if (i == 0):
                stack.append(tuple((temperatures[i], i)))
            elif (curr <= prev):
                stack.append(tuple((curr, i)))
            else: # curr > prev
                next_largest = i
                while (stack and stack[-1][0] < curr):
                    top_index = stack[-1][1]
                    stack.pop()
                    result[top_index] = next_largest - top_index
            prev = temperatures[i]
            stack.append(tuple((curr, i)))
        
        while stack:
            top_index = stack[-1][1]
            stack.pop() 
            result[top_index] = 0
        
        return result
        





class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)
        
        # [1, 2, 8, 48]

        postfix = [1] * len(nums)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            postfix[i] = product
        # [48, 48, 24, 6]

        # prefix[i] * postfix[i + 1]

        output = []

        for i in range(len(nums)):
            if (i == 0): 
                output.append(postfix[i + 1])
            elif (i == len(nums) - 1):
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * postfix[i + 1])
        
        return output

        






        
        





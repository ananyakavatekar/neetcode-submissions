class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # recheck this bruh
        prefix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else: 
                prefix.append(nums[i] * prefix[i-1])
        

        suffix = [0] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else: 
                suffix[i] = (nums[i] * suffix[i + 1])

        output = []

        for i in range(len(nums)):
            if i == 0:
                output.append(suffix[i + 1])
            elif i == len(nums) - 1: 
                output.append(prefix[i - 1])
            else: 
                output.append(prefix[i - 1] * suffix[i + 1])
        
        return output


            


        






        
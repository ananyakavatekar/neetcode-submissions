class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums = sorted(nums)
        target = 0
        output = []
      
        for i in range(len(nums)):
            a = nums[i]
            if (i > 0 and a == nums[i - 1]): # prevents duplicates
                continue
            left = i + 1 # 1 to the right of a
            right = len(nums) - 1 # -1 to ensure index in bounds
            while (left < right):
                current_sum = a + nums[left] + nums[right]
                if (current_sum > target):
                    right -= 1
                elif (current_sum < target):
                    left += 1
                else: # current_sum == target
                    output.append([a, nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
        return output

        




        
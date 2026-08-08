class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        difference_map = {}

        for i in range(len(nums)):
            if ((target - nums[i]) in difference_map):
                return [difference_map[target - nums[i]], i]
            difference_map[nums[i]] = i
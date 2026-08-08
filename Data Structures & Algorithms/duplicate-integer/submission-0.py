class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = []

        for i in range(len(nums)):
            if (nums[i] in stack):
                return True
            else:
                stack.append(nums[i])
        return False
        
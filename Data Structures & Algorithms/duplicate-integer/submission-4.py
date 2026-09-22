class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        existing = set()

        for i in range(len(nums)):
            if (nums[i] in existing):
                return True
            existing.add(nums[i])
        
        return False
        
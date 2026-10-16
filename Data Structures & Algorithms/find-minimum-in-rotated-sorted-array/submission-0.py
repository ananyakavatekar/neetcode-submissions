class Solution:
    def findMin(self, nums: List[int]) -> int:

        asc = True

        min_val = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            if (nums[i] < prev):
                min_val = nums[i]
                break
        
        return min_val

        
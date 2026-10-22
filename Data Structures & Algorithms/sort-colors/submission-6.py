class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                # if there was a right swap don't increment i
                right -= 1
                i -= 1
            i += 1
            






        
        
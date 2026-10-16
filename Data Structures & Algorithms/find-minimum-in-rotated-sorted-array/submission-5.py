class Solution:
    def findMin(self, nums: List[int]) -> int:

        # no mater how many rotations we will have either 1 or 2 sorted segments in the array
        # use binary search to find it. 
        # 3 ptrs, left, right, and middle
        # at least 2 of these 3 pts will always be in the same sorted segment
        # we can confirm this by seeing which two in order ptrs follow the strictly ascending rule
        left = 0 
        right = len(nums) - 1

        while (left < right):
            mid = (left + right) // 2
            if (nums[mid] > nums[right]):
                # min val is to the right
                left = mid + 1
            else: 
                # min val is at mid or to its left
                right = mid
    
        return nums[left]
        






        
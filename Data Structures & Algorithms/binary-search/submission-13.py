class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if (target < nums[0] or target > nums[-1]): 
            return -1
        
        # "//" does floor divsion and returns a whole number
        left = 0
        right = len(nums) - 1
        while (left <= right): 
            mid_ptr = ((right + left)//2)
            if (nums[mid_ptr] == target):
                return mid_ptr
            elif (nums[mid_ptr] < target):
                left = mid_ptr + 1
            else: # target is to the left (smaller) of mid ptr
                right = mid_ptr - 1
        return -1



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if (len(heights) < 2):
            return 0

        left = 0
        right = len(heights) - 1

        bucket_height = min(heights[left], heights[right])
        bucket_width = right - left

        max_area = bucket_height * bucket_width

        while (left < right):
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)
            if (heights[left] < heights[right]):
                left += 1
            else: 
                right -= 1
        
        return max_area



        
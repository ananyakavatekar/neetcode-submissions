class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)   
        index = 0 
        right = 0
        while (right < len(ans)):
            ans[right] = nums[right % len(nums)]
            right += 1
    
        return ans



class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)   
        right = 0 # index in the ans array
        while (right < len(ans)):
            ans[right] = nums[right % len(nums)]
            right += 1
        return ans



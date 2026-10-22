class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = defaultdict(int)
        maxCount = 0
        majority = 0

        for n in nums:
            freq[n] += 1
            if (freq[n] > maxCount):
                maxCount = freq[n]
                majority = n
        
        return majority





        
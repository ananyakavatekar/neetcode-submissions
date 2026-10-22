class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = len(nums) // 2

        freq = defaultdict(int) 

        majority_num = 0
        maxCount = 0

        for n in nums: 
            freq[n] += 1 
            if freq[n] > maxCount:
                maxCount = freq[n]
                majority_num = n
        
        
        return majority_num



        
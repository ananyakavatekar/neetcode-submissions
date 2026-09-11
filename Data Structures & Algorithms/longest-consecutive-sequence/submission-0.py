class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums);
        longest = 0 
        for num in nums_set: 
            curr_run = 1
            if ((num - 1) not in nums_set):
                next_num = num + 1
                while next_num in nums_set:
                    curr_run += 1
                    next_num += 1
                if (curr_run > longest):
                    longest = curr_run
        
        return longest
                    



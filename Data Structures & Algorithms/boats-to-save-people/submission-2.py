class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        ppl_sorted = sorted(people) # O(nlogn)

        boats_needed = 0
        left = 0 
        right = len(ppl_sorted) - 1
        
        while left <= right: 
            if (ppl_sorted[left] + ppl_sorted[right] > limit):
                boats_needed += 1
                right -= 1
            else: #they are less than or equal to
                boats_needed += 1
                left += 1 
                right -= 1
        
        return boats_needed





        
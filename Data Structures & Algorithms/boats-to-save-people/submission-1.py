class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # theres at least 2 ppl in the starting list

        ppl_sorted = sorted(people)

        # boat can only carry 2 people

        boats_needed = 0
        left = 0 
        right = len(ppl_sorted) - 1

        while (right > 0 and ppl_sorted[right] == limit):
            boats_needed += 1 
            right -= 1 
        
        while left <= right: 
            if (ppl_sorted[left] + ppl_sorted[right] > limit):
                boats_needed += 1
                right -= 1
            else: #they are less than or equal to
                boats_needed += 1
                left += 1 
                right -= 1
        
        return boats_needed





        
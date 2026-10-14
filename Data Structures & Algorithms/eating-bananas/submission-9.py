class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:



        # there is a monotonic relationship between k and h 
        # as k increases -> h strictly decreases
    
        # the greatest k can be is the size of the largest pile in piles
        # the smallest k can be is 1 otherwise koko never makes progress on  any of the piles
        # search space is [1, max(piles)]

        # full range to search [1, max(piles)]
        # left ptr at 1, right at max(piles) search middle towards

        left = 1
        right = max(piles)

        best_k = max(piles)
        while left <= right:
            k = (right + left) // 2 # floor divison
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)
            
            if (hours_needed > h):
                left = k + 1
            else: # (hours_needed <= h)
                if (k < best_k):
                    best_k = k
                right = k - 1
        
        return best_k
        



            
             

        
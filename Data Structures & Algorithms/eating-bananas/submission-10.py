class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        # [1, max(piles)]

        # math.ciel(piles[i] / k) = # hours required to eat a pile
    # [25, 10, 23, 4] h = 4
        left = 1
        right = max(piles)
        best_k = float("inf")
        while left <= right:
            hours_needed = 0
            mid = (left + right) // 2
            for pile in piles: 
                hours_needed += math.ceil(pile / mid)
            if (hours_needed > h):
                left = mid + 1
            else: # hours_needed <= h
                best_k = min(best_k, mid)
                right = mid - 1
            
        return best_k



        
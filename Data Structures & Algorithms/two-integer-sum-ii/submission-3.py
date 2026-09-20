class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer instead of hashmap solution ensures that space complexity is O(1) instead of O(n)
        # left and right index take advantage of nums being sorted
        left = 0
        right = len(numbers) - 1

        # since its sorted left num is smaller than right num
        current_sum = numbers[left] + numbers[right]
        
        while (current_sum != target): 
            if (current_sum > target):
                # make right num smaller
                right -= 1
            if (current_sum < target):
                # make left num bigger
                left += 1
            current_sum = numbers[left] + numbers[right]
        # adding one cuz indexed at 1 constraint 
        return [left + 1, right + 1]

        


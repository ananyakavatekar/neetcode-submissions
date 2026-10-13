class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(arr, left, right):
            # base case
            if left == right: 
                return arr
            
            mid = (left + right) // 2
            mergesort(arr, left, mid)
            mergesort(arr, mid + 1, right)

            merge(arr, left, mid, right)
            return arr
        
        def merge(arr, left, mid, right):
            
            # i is supposed to point to the start of the merged sub array
            # j and k are points to the first element of the left and right sub array
            i, j, k = left, 0, 0
            
            left = arr[left:mid + 1]
            right = arr[mid + 1:right + 1]

            while j < len(left) and k < len(right): 
                if (left[j] <= right[k]):
                    # since the left is smaller it will be the start in the arr
                    arr[i] = left[j]
                    j += 1
                else: 
                    arr[i] = right[k]
                    k += 1
                i += 1
            # in the condition that they are different sizes
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        return mergesort(nums, 0, len(nums) - 1)
        



        
            






        



        
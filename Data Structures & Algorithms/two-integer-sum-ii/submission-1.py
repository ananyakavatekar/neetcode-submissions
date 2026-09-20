class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # complement = target - nums[i]

        complements = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if (complement in complements):
                # the other of this return makes sure index1 < index2
                # i + 1 here makes sure we access correct index but return 1-indexed
                return ([complements[complement], i + 1])
            complements[numbers[i]] = i + 1
        


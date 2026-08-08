class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequncy of elements w/ dict
        freq = {}
        for num in nums: 
            if num not in freq: 
                freq[num] = 1
            else: 
                freq[num] += 1

        # sort dict by values (frequency) in descending order

        sorted_dict = dict(sorted(freq.items(), key= lambda item: item[1], reverse=True))

        # return top k elements by frequency

        elements = list(sorted_dict.keys())

        res = []

        for i in range(k):
            res.append(elements[i])
        
        return res
            



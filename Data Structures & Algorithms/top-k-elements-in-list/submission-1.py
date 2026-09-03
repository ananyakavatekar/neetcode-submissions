class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = []
        for i in range(len(nums)):
            buckets.append([])

        freq_map = defaultdict(int)
        for i in range(len(nums)):
            freq_map[nums[i]] += 1

        for number, freq in freq_map.items():
            buckets[freq - 1].append(number)
        
        final_list = []
        buckets = buckets[::-1]
        while len(final_list) != k: 
            for i in range(len(buckets)):
                for j in range(len(buckets[i])):
                    if (len(final_list) < k):
                        final_list.append(buckets[i][j])
        
        return final_list


        



        


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = defaultdict(int)

        for i in range(len(nums)):
            freq_map[nums[i]] += 1
        
        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        for key, val in freq_map.items(): 
            buckets[val].append(key)
        
        buckets = buckets[::-1]

        output = []
        for bucket in buckets: 
            i = 0
            val_count = len(bucket)
            while len(output) < k and i < val_count: 
                output.append(bucket[i])
                i += 1
        return output

        
        
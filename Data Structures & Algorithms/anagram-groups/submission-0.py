class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # make the count a tuple since dict keys have to be hashable
            res[tuple(count)].append(s)
        
        return list(res.values())

        

        
                
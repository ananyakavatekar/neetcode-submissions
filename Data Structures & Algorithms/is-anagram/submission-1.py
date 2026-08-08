class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_counts = {}

        t_counts = {}

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if (s[i] not in s_counts.keys()):
                s_counts[s[i]] = 0
            if (t[i] not in t_counts.keys()):
                t_counts[t[i]] = 0
            s_counts[s[i]] += 1
            t_counts[t[i]] += 1
        
        return s_counts == t_counts

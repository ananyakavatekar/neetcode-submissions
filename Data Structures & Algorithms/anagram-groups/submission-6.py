class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_freq_map = defaultdict(list)
        # creates a array of set size 26 imputed with 0s
        for word in strs:
            freq_arr = [0] * 26
            for letter in word: 
                # Ascii 97 - 122 is the alphabet lower case
                freq_arr[ord(letter) - 97] += 1
            strs_freq_map[tuple(freq_arr)].append(word)
        
        grouped = list(strs_freq_map.values())
        return grouped

        
        

        


        
        

        






        

        
                
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for phrase in strs: 
            phrase_len = len(phrase)
            encoded_string += str(phrase_len) + "#" + phrase
        
        return encoded_string

    def decode(self, s:str) -> List[strs]: 
        decoded_lst = []
        i = 0
        while i < len(s): 
            if (s[i].isdigit()):
                j = i 
                while(s[j].isdigit()):
                    j += 1
                phrase_len = int(s[i:j])
                if (s[j] == "#"):
                    j += 1
                extracted_phrase = s[j : j + phrase_len]
                decoded_lst.append(extracted_phrase)
                i = j + phrase_len
        
        return decoded_lst

                





            

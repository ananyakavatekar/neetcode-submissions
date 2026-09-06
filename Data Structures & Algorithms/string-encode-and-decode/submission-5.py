class Solution:

    def encode(self, strs: List[str]) -> str:
        # takes a list of string and packs into a single string
        encoded_string = ""

        for phrase in strs:
            phrase_len = len(phrase)
            encoded_string += str(phrase_len) + "#" + phrase
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # takes the packaged string and returns original list containing strings
        decoded_lst = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j] != "#":
                    j += 1
                phrase_len = int(s[i:j])
                extracted_phrase = s[j+1:j + phrase_len + 1]
                decoded_lst.append(extracted_phrase)
                i = j + 1 + phrase_len
        return decoded_lst

            

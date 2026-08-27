class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for i in s: 
            if i.isalnum():
                cleaned_s += i

        return cleaned_s.lower() == cleaned_s[::-1].lower()



        
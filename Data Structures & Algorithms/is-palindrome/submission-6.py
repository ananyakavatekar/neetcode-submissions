class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ""

        for i in range(len(s)):
            if (s[i].isalnum()):
                letters += s[i].lower()
        

        return letters == letters[::-1]

        
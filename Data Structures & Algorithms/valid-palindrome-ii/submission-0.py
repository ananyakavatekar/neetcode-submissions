class Solution:
    def validPalindrome(self, s: str) -> bool:


        # same forward and backward without deleteing

        if (s == s[::-1]):
            return True
        
        # now try deleting process 

        for i in range(len(s)):
            if (i <= len(s) - 2):
                with_removed = s[:i] + s[i+1:]
            if (i == len(s) - 1):
                # end is not included
                with_removed = s[:i]
            if (with_removed == with_removed[::-1]):
                return True


        return False
        
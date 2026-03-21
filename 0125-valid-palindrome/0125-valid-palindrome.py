class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        h = len(s) - 1

        while l < h:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[h].isalnum():
                h -= 1
                continue
            if s[l] != s[h]:
                return False

            l += 1
            h -= 1
        return True
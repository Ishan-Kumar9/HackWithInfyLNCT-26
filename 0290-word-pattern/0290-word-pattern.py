class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapp = {}
        used = set()
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i in range(len(s)):
            if pattern[i] not in mapp:
                if s[i] in used:
                    return False
                mapp[pattern[i]] = s[i]
                used.add(s[i])
            else:
                if mapp[pattern[i]] == s[i]:
                    continue
                else:
                    return False
        return True
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        else:
            phrase = []
            sorted_list = sorted(strs)
            a = sorted_list[0]
            b = sorted_list[-1]
            minn = min(len(a), len(b))
            for i in range(minn):
                if a[i] == b [i]:
                    phrase.append(a[i])
                else:
                    break
            result = ''.join(phrase)
            if len(phrase) > 0:
                return result
            else:
                return ''
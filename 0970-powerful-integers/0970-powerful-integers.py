class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i = 0
        res = set()
        while x**i <= bound:
            j = 0
            while y**j <= bound:
                val = x**i + y**j
                if val<=bound:
                    res.add(x**i + y**j)
                else:
                    break
                if y == 1:
                    break
                j += 1
            if x == 1:
                break
            i += 1
        return sorted(list(res))
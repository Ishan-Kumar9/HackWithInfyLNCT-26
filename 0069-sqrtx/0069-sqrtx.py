class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        h = x // 2
        while l <= h:
            mid = (l+h)//2
            m = mid * mid
            if m == x:
                return mid
            elif m > x:
                h = mid - 1
            else:
                l = mid + 1
        
        return h
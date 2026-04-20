class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        h = num
        while l <= h:
            mid = (l+h)//2
            m = mid**2
            if m == num:
                return True
            elif m > num:
                h = mid - 1
            else:
                l = mid + 1
        return False
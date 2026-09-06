class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        score = 0
        summ = sum(nums)
        mid = n//2
        new = nums + nums
        pre = 0
        for i in range(mid):
            pre += nums[i]
        post = summ - pre

        for j in range(n):
            if pre > post:
                score += 1
            pre -= new[j]
            post += new[j]
            post -= new[mid+j]
            pre += new[mid+j]
        return score
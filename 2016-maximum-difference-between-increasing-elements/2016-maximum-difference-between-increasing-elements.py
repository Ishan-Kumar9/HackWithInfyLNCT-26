class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx = -1
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                d = nums[j] - nums[i]
                if d == 0:
                    continue
                maxx = max(maxx, d)
        return maxx
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxx = 0
        nums.sort()

        for i in range(1,len(nums)):
            gap = nums[i] - nums[i-1]

            if gap > maxx:
                maxx = gap

        return maxx
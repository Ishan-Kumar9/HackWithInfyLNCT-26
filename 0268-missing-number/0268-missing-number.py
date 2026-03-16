class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        for num in nums:
            summ += num

        total_summ = n*(n+1)//2
        return total_summ - summ
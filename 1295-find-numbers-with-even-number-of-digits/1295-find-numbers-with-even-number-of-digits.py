class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            n = len(nums[i])
            if n%2 == 0:
                count += 1
        return count
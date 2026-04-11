class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        miss = []
        n = len(nums)
        nums = set(nums)
        for i in range(n):
            if i+1 not in nums:
                miss.append(i+1)
        return miss 
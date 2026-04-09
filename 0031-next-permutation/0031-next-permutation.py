class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >=0 and nums[i] >= nums[i+1]:
            i -= 1
        pivot = i

        if pivot >= 0:
            for j in range(len(nums)-1,pivot,-1):
                if nums[j] > nums[pivot]:
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
        nums[pivot+1:] = reversed(nums[pivot+1:])
        return
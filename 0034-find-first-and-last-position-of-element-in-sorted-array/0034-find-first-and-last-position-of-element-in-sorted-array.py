class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        h = len(nums) - 1
        first = -1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                first = mid
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        l, h = 0, len(nums)-1
        last = -1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return [first, last]
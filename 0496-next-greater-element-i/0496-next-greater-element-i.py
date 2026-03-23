class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = [-1]*len(nums1)

        for i in range(len(nums1)):
            for j in range(len(nums2)-1):
                if nums1[i] == nums2[j] and nums2[j+1] > nums2[j]:
                    nums3[i] = nums2[j+1]
        return nums3
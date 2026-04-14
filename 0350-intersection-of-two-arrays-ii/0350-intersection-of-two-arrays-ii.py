class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        for i in set(nums1):
            c1 = nums1.count(i)
            c2 = nums2.count(i)
            m = min(c1,c2)
            inter.extend([i]*m)
        return inter
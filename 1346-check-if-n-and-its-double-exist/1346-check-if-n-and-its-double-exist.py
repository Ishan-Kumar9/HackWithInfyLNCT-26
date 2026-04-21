class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr1 = set(arr)
        for i in arr1:
            if 2 * i in arr1:
                return True
        return False
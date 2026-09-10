class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        left = 0
        summ = 0
        for right in range(len(arr)):
            summ += arr[right]

            if right-left+1 > k:
                summ -= arr[left]
                left += 1
            n = right -left+1
            if n == k and summ/n >= threshold:
                cnt += 1
        return cnt
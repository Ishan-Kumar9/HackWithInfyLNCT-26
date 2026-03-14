class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in digits:
            sum = sum * 10 + i
        sum += 1
        result = []
        a = str(sum)
        for i in a:
            result.append(int(i))
        
        return result
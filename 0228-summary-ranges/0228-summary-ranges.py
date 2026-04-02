class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        temp = []
        while i<len(nums)-1:
            if nums[i+1] == nums[i] + 1:
                if not temp:
                    temp.append(nums[i])
                temp.append(nums[i+1])
                i += 1
            else:
                if not temp:
                    res.append(str(nums[i]))
                if len(temp) == 1:
                    res.append(str(temp[0]))
                elif len(temp) > 1:
                    res.append(str(temp[0])+"->"+str(temp[-1]))
                temp.clear()
                i += 1

        if temp:
            if len(temp) == 1:
                res.append(str(temp[0]))
            else:
                res.append(str(temp[0])+"->"+str(temp[-1]))
        elif i == len(nums) - 1:
            res.append((str(nums[i])))

        return res
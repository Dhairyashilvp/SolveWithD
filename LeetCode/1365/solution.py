class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        for e in nums:
            for n in nums:
                if n < e:
                    count += 1
            ans.append(count)
            count = 0
        return ans
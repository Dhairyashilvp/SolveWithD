class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for k, v in enumerate(nums[:-2]):
            if k >= 1 and v == nums[k-1]:
                continue
            d = {}
            for x in nums[k + 1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    ans.add((v, -v-x, x))
        return ans
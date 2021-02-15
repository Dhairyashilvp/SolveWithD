class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        for j in range(1,l):
            if nums[j] != nums[j-1]:
                i += 1
                nums[i] = nums[j]
        return i+1
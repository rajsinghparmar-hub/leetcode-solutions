class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0 

        l = 0 

        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1
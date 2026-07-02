class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = False
        b = len(nums)
        nums.sort()
        for i in range(b-1):
            if (nums[i] == nums[i+1]):
                a = True
                break
            else:
                a = False
        return a
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return False if len(set(nums)) == len(nums) else True

x = Solution()

nums_1 = [1,2,3,1]
nums_2 = [1, 3, 2]
print(x.containsDuplicate(nums_2))


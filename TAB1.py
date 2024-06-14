nums = [2, 7, 11, 15],
target = 9
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nt = {}
        for index, num in enumerate(nums):
            x = target - num
            if x in nt:
                return [index,nums.index(x)]
            
            nt[num] = index
            return

            
                   

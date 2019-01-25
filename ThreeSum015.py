#   File Name:           ThreeSum015     
#   Description:
#   Author:              midasevil
#   date:                2018/10/13
#

__author__ = 'midasevil'


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        result = ()
        for i in range(0, l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.([nums[i],nums[j],nums[k]])

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([2, -1, -1, 0, 2, -1]


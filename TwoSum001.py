#   File Name:           TwoSum     
#   Description:
#   Author:              midasevil
#   date:                2018/10/13
#


__author__ = 'midasevil'


class Solution(object):
    def twoSum_brute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(0, l - 1):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_hash(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int
        """
        map = dict()
        l = len(nums)
        for i in range(l):
            if nums[i] in map:
                return [map[nums[i]], i]
            else:
                map[target - nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    assert [0, 2] == s.twoSum_brute([2, 3, 5], 7)
    assert [0, 2] == s.twoSum_hash([2, 3, 5], 7)

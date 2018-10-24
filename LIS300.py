#   File Name:           LIS300     
#   Description:
#   Author:              midasevil
#   date:                2018/10/14
#

__author__ = 'midasevil'


class Solution:
    def __init__(self):
        self.bag = {}

    def lengthofLIS(self, n, nums):
        if n == 0:
            return 1
        if n in self.bag:
            return self.bag[n]

        car = 0
        for i in range(n):
            if nums[n] > nums[i]:
                if self.lengthofLIS(i, nums) > car:
                    car = self.lengthofLIS(i, nums)
        self.bag[n] = car + 1
        return car + 1

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_lis = 1
        len_nums = len(nums)

        if len_nums == 0:
            return 0
        for n in range(len_nums):
            len_lis = max(len_lis,self.lengthofLIS(n, nums))
        print(self.bag)
        return len_lis



class Solution_dp:
    def lengthOfLIS(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        dp = [1] * len(nums)

        for i in range(1,l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i] , dp[j] + 1)


        return max(dp)


a = 1
a += 1
print(a)
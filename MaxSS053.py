class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [0]*nums_len
        dp[0] = nums[0]
        for i in range(1,nums_len):
            if dp[i-1] < 0 :
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]

        return max(dp)

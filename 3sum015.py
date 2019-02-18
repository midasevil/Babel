class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums_len =  len(nums)
        res = []
        for i in range(nums_len-2):
            for j in range(i+1,nums_len-1):
                for z in range(j+1,nums_len):
                    if nums[i] + nums[j] + nums[z] == 0:
                        target = [nums[i],nums[j],nums[z]]
                        target = sorted(target)
                        if target not in res:
                            res.append(target)
        return res








nums = [-1, 0, 1, 2, -1, -4]
res = [
  [-1, 0, 1],
  [-1, -1, 2]
]

s = Solution()
print(s.threeSum(nums))
assert s.threeSum(nums) == res
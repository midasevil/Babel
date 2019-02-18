class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        nums_len = len(nums)
        res =  sum(nums[:3])
        for i in range(nums_len-2):
            l = i + 1
            r = nums_len - 1
            while r > l :
                cur = sum(nums[i],nums[l],nums[r])
                if abs(cur-target) < abs(res-target):
                    res = cur
                if cur - target > 0:
                    r = r - 1
                else:
                    l = l + 1
        return res
class Solution:
    def threeSum_Force(self, nums: 'List[int]') -> 'List[List[int]]':
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

    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for l in range(0,len(nums)-2):
            i=l+1
            r=len(nums)-1
            while i<r and i>l:
                sum=nums[l]+nums[r]+nums[i]        
                if sum==0:
                    a=[nums[l],nums[i],nums[r]]
                    ans.append(a)
                    i+=1
                elif sum>0:
                    r-=1
                else: 
                    i+=1
                    
        ans = set(map(tuple, ans))
        return list(ans)








nums = [-1, 0, 1, 2, -1, -4]
res = [
  [-1, 0, 1],
  [-1, -1, 2]
]

s = Solution()
print(s.threeSum(nums))
assert s.threeSum(nums) == res
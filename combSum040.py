class Solution:
    def combinationSum2(self, candidates,target):
        ans = []
        fp_check = []
        cand_len = len(candidates)
        def dfs(s=[],i=0):
            if sum(s) == target:
                fp = hash(tuple(sorted(s)))
                if fp not in fp_check:
                    ans.append(list(s))
                    fp_check.append(fp)
            for n in range(i,cand_len):
                s.append(candidates[n])
                dfs(s,n+1)
                s.pop()
        dfs()
        print(ans)
        return ans
s = Solution()
s.combinationSum2([2,5,1,1,2,3,3,3,1,2,2],5)

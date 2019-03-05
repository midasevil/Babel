class Solution:
    def combinationSum(self, candidates,target):
        candidates.sort()
        ans = []
        cand_len = len(candidates)
        def dfs(s=[],i=0):
            if sum(s) == target:
                ans.append(list(s))
                return
            if sum(s) > target:
                return
            else:
                for n in range(i,cand_len):
                    s.append(candidates[n])
                    dfs(s,n)
                    s.pop()

        dfs()
          
        print(ans)

s = Solution()
s.combinationSum([2,3,6,7],6)




# cand = [2,3,6] 
# n = 3  
# ans = []     
# def  generate(s=[],cand=cand):
#     print(s)
#     if cand == []:
#         return
#     if len(s) == n:
#         ans.append(list(s))
#     s.append(cand[0])
#     generate(s,cand[1:])
#     s.pop()
# generate()
# print(ans)

# l = []
# s = []
# for i in "abc":
#     l.append(i)
#     s.append(l)
# print(s)


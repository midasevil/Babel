class Solution:
    def generateParenthesis(self, n):
        ans = []
        def backtrack(s,left,right):
            if len(s) == 2*n:
                ans.append(s)
            if left < n:
                backtrack(s+'(',left+1,right)
            if right < left:
                backtrack(s+')',left,right+1)
        backtrack("",0,0)
        print(ans)

s = Solution()
s.generateParenthesis(3)
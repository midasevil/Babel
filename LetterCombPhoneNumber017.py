class Solution:
    def letterCombinations(self, digits):
        bag = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def backtrack(load,digits):
            if digits == "":
                res.append(load)

            else:
                chars = bag[digits[0]]
                for c in chars:
                    backtrack(load+c,digits[1:])
        if digits == "":
            return []
        else:
            backtrack("",digits)
            return res        


s = Solution()
print(s.letterCombinations("235"))
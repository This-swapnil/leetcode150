# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8


from re import L


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # only add open parenthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IF open==closed==n

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


n = 3
s = Solution()
print(s.generateParenthesis(n=n))

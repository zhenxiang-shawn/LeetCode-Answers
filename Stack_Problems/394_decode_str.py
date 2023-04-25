"""
执行用时：32 ms, 在所有 Python3 提交中击败了86.01%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了78.74%的用户
通过测试用例：34 / 34
"""


class Solution:
    def decodeString(self, s: str) -> str:
        multi = 0
        ans = ""
        stack = []
        for c in s:
            if c.isnumeric():
                multi = multi * 10 + int(c)
            elif c == '[':
                # Due to getting in the new bracket, save current ans to stack.
                stack.append((multi, ans))
                multi, ans = 0, ""
            elif c == ']':
                # end of bracket, pop element from stack and convert it to string
                (saved_multi, saved_ans) = stack.pop()
                ans = saved_ans + saved_multi * ans
            else:
                ans += c
        return ans


Solution = Solution()

# Input: s = "3[a]2[bc]"
s = "3[a]2[bc]"
# Output: "aaabcbc"
print(Solution.decodeString(s))

# Input: s = "3[a2[c]]"
s = "3[a2[c]]"
print(Solution.decodeString(s))
# Output: "accaccacc"


# Input: s = "2[abc]3[cd]ef"
s = "2[abc]3[cd]ef"
print(Solution.decodeString(s))
# Output: "abcabccdcdcdef"

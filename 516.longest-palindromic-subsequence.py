#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def rec(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 2 + rec(l+1, r-1)
            else:
                
                return max(rec(l+1, r), rec(l, r-1))

        return rec(0, len(s)-1)


# @lc code=end

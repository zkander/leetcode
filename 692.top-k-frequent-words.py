#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

from collections import defaultdict

# @lc code=start


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        d = defaultdict(int)

        for i in range(len(words)):
            d[words[i]] += 1

        sWords = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        sDic = dict(sWords)

        ans = list(sDic.keys())

        return ans[:k]


# @lc code=end

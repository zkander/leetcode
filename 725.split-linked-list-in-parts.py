#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        temp = head
        parts = []
        while temp:
            count += 1
            temp = temp.next

        base, extra = divmod(count, k)
        cur = head
        dummy = ListNode()
        for _ in range(k):
            print(cur)
            parts.append(cur)
            for _ in range(base + (extra > 0)):
                dummy = cur
                cur = cur.next

            if (extra > 0):
                extra -= 1
                
            dummy.next = None
        print(parts)
        return parts

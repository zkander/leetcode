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
        print(head)
        arr = []
        while temp:
            if temp:
                arr.append(temp.val)
                count += 1
                temp = temp.next
        print(arr)
        dic = dict()
        for i in range(k):
            dic[i] = []
        j = 0
        for i in range(len(arr)):
            dic[j].append(arr[i])
            j += 1
            if j > k - 1:
                j = 0

        ans = list(dic.values())
        print(ans)
        ls = []
        for i in range(len(ans)):
            temp = ListNode(ans[i][0], None)
            for j in range(len(ans[j])):
                temp.next = temp

        return ls

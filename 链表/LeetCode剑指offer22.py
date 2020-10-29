# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = ListNode(-1)
        new_head.next = head
        p = new_head
        q = new_head
        while p:
            if k > 0:
                p = p.next
                k = k - 1
            else:
                q = q.next
                p = p.next
        return q.val


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    k = 2
    solve = Solution()
    result = solve.getKthFromEnd(a, k)
    while result:
        print(result.val)
        result = result.next
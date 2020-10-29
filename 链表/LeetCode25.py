# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head


    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        hair = ListNode(-1)
        hair.next = head
        pre = hair
        while head:
            tail = hair
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            # 进行单链表反转
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next


if __name__ == "__main__":
    solve = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    k = 2
    print(type(a))
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    result = solve.reverseKGroup(a, k)
    while result:
        print(result.val, "->")
        result = result.next

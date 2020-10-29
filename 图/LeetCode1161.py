# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        my_queue = collections.deque()
        my_queue.append({
            "node":root,
            "dept":1
        })
        val_hash = collections.defaultdict(int)
        while my_queue:
            my_node = my_queue.popleft()
            node = my_node.get("node")
            dept = my_node.get("dept")
            val_hash[dept] += node.val
            if node.left:
                my_queue.append({
                    "node": node.left,
                    "dept": dept+1
                })
            if node.right:
                my_queue.append({
                    "node": node.right,
                    "dept": dept + 1
                })
        #print(val_hash)
        max_index = 0
        sum_max = 0
        for key, val in val_hash.items():
            if sum_max < val:
                sum_max = val
                max_index = key
        return max_index


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(1)
    b = TreeNode(7)
    c = TreeNode(0)
    d = TreeNode(7)
    e = TreeNode(-8)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    result = solve.maxLevelSum(a)
    print(result)
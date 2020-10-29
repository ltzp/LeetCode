# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        vals = []
        self.dfs(root, vals)
        head = TreeNode(vals[0])
        node = head
        for i in range(1, len(vals)):
            node.right = TreeNode(vals[i])
            node = node.right
        return head

    def dfs(self, node, vals):
        if node == None:
            return node
        self.dfs(node.left, vals)
        vals.append(node.val)
        self.dfs(node.right, vals)



if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(6)
    d = TreeNode(2)
    i = TreeNode(4)
    e = TreeNode(8)
    f = TreeNode(1)
    g = TreeNode(7)
    h = TreeNode(9)
    a.left = b
    a.right = c
    b.left = d
    b.right = i
    c.right = e
    d.left = f
    e.left = g
    e.right = h
    solve = Solution()
    result = solve.increasingBST(a)
    print(result.val)
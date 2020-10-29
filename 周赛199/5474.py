# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 0
        res = 0
        left_distance = []
        right_distance = []
        if root.left:
            self.dfs(root.left, left_distance, 0)
            for i in range(len(left_distance)):
                for j in range(i + 1, len(left_distance)):
                    num = left_distance[i] - left_distance[j]
                    if abs(num) <= distance:
                        res = res + 1
        if root.right:
            self.dfs(root.right, right_distance, 0)
            for i in range(len(right_distance)):
                for j in range(i + 1, len(right_distance)):
                    num = right_distance[i] - right_distance[j]
                    if abs(num) <= distance:
                        res = res + 1
        if left_distance and right_distance:
            for i in range(len(left_distance)):
                for j in range(len(right_distance)):
                    if left_distance[i] + right_distance[j] <= distance:
                        res = res + 1
        return res

    def dfs(self, node, node_distance, length):


        length = length + 1
        if not node.left and not node.right:
            node_distance.append(length)
            return node_distance
        if node.left:
            self.dfs(node.left, node_distance, length)
        if node.right:
            self.dfs(node.right, node_distance, length)


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    solve = Solution()
    distance = 3
    result = solve.countPairs(a, distance)
    print(result)

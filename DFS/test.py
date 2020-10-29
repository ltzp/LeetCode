class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # leetcode submit region end(Prohibit modification and deletion)
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        l_p = preorder[1:index + 1]
        r_p = preorder[index + 1:]
        l_i = inorder[0:index]
        r_i = inorder[index + 1:]
        node.left = self.buildTree(l_p, l_i)
        node.right = self.buildTree(r_p, r_i)
        return node


def range_tree(root):
    if not root:
        return
    range_tree(root.left)
    print(root.val)
    range_tree(root.right)


if __name__ == '__main__':
    sol = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    ans = sol.buildTree(preorder, inorder)
    range_tree(ans)
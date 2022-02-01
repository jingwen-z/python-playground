# Easy
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
# reference: https://ao.ms/how-to-get-the-maximum-depth-of-a-binary-tree-in-python/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)

        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1

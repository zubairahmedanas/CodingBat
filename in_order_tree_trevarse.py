# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
	def inorderTraversal(root):
		res = []
		stack = []
		# print("lets see", stack)
		while root or stack:
			# print("lets see")
			while root is not None:
				stack.append(root)
				root = root.left
			root = stack.pop()
			res.append(root)
			print("the result is", res)
			root = root.right
		return res

	root = [1,2,3,4]
	print(inorderTraversal(root))




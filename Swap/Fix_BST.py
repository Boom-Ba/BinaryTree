#find a paired of nodes that is incorrectly placed in BST, and sawp them
import sys
class Solution:

	'''
	A binary tree node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''
	#use previous node to check the property of BST
	def fixBinaryTree(self, root: Node) -> None:
		if not root:
			return None
		def find_incorrect_nodes(root,x,y,prev=Node(-sys.maxsize) ):
			
			if not root:#empty tree
				return x,y,prev #can't find incorrect nodes 
		
			#each time, previous node must be less than the root node
			#because inorder visiting left, root, right, so the left.val has to be less than the root.val
			x,y,prev =find_incorrect_nodes(root.left,x,y,prev)
			
			if root.data<prev.data: #root< left (prev)
				if not x:
					x=prev
				y=root
			#not found in the LST, call right 
			prev=root
			return find_incorrect_nodes(root.right,x,y,prev)
			
		def swapData(first, second):
 
		    data = first.data
		    first.data = second.data
		    second.data = data
		x,y,prev=find_incorrect_nodes(root,None,None)
	
		if x and y:
			swapData(x,y)
		

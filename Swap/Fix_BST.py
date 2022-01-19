def fixBinaryTree(self, root: Node) -> None:
	
	"""
	Inorder traverse the tree
	Note: incorrect traverse expect an increasing order. so if node value placed as a reversed order, which means a pair of node has been placed incorrectly.
		1. If prev traversed node has value that is greater than the current node, the prev is place incorrectly, need to be marked for swapping.
		2. We might found two pairs of reversed order because the incorrectly nodes have been placed on the two sides of root.
		3. If we only found one pair of incorrectly reversed nodes, means, the incorrect nodes have been placed on the one side of root, like
		3. 5
	      5.     3
		
	"""
	
	def correct(root,x, y, prev):
		if root is None:
			return x, y, prev
		#Left First 
		x,y,prev=correct(root.left,x,y,prev)
		#check 
		if root.data < prev.data:
			if x is None:
				x=prev 
				
			y=root
		#if no found such case, keep checking the RST
		prev=root
		return correct(root.right,x,y,prev)

	x = None
	y=  None
	prev= Node(-sys.maxsize)
	x,y,prev= correct(root,x,y,prev)
	if x and y:
		x.data,y.data=y.data,x.data
	
			
	

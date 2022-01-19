def constructBST(self, preorder: List[int]) -> Node:
	# Write your code here...
	
	def construct(preorder, start, end):
		if not preorder:
			return 
		if start>end:
			return
		root=Node(preorder[start])
		#construct a root node
		i = start #create an index point to start of preorder
		while i<=end:
			if preorder[i]>root.data:
				break
			i+=1
		root.left=construct(preorder, start+1, i-1)
		root.right=construct(preorder, i, end)
		return root 
	if not preorder:
		return None

	return construct(preorder, 0,len(preorder)-1)

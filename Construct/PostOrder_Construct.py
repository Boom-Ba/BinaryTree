"""
Use bound to recursively construct LST and RST
"""
def constructBST(self, postorder: List[int]) -> Node:
	def construct(start, end ):
		if start>end:
			return None 

		val =postorder[end]
		root =Node(val)
		end-=1
		index=end
		while index>=0:
			if postorder[index]<val:
				break
			index-=1

		root.left= construct(start, index)
		root.right =construct(index+1, end)

		return root 

	if not postorder:
		return None 
	return construct( 0, len(postorder)-1 )

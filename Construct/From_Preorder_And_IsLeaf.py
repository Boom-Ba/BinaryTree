"""
construct Tree from pre-order and isLeaf
preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7]      Root Left Right
isLeaf    =[0, 0, 1, 1, 0, 0, 1, 1, 1]
            1
        2      3      
      4   5   6  7
            8  9
            
"""
def constructBinaryTree(self, preorder: List[int], isLeaf: List[int]) -> Node:
		# Write your code here...
		
		if not preorder: return None
		index=0
		def help(preorder,isLeaf,index):
			root=Node(preorder[index]) #make a node at root index
			#check if is internal node or leaf
			#if is internal: continue constructing left and right for it
			internal = (isLeaf[index] ==0)
			index+=1
			if internal:
				root.left,index =help(preorder,isLeaf,index)
				root.right,index =help(preorder,isLeaf,index)
			return root,index
		return help(preorder,isLeaf,index)[0]

# time: n^2
def findLargestBSTSize(self, root: Node) -> int:
	
	def size(root):
		if not root:
			return 0 
		leftSize =size(root.left ) if root.left else 0
		rightSize =size(root.right) if root.right else 0
		return leftSize+rightSize + 1 
	
	def ValidBST(root,min_,max_):
		if not root:
			return True 
			
		if root.data< min_ or root.data>max_:
			return False 
		return ValidBST(root.left,min_,root.data) and ValidBST(root.right,root.data, max_)
	
	if not root:
		return 0 
	if ValidBST(root,-sys.maxsize,sys.maxsize):
		return size(root)

	return max(self.findLargestBSTSize(root.left),self.findLargestBSTSize(root.right))

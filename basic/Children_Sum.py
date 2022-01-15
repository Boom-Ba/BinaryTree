#ret value is the sum of LST and RST
#if found the sum is equal to root.val, ret root.val
#else ret float('inf') means inaccessible 
def checkChildrenSumProperty(self, root: Node) -> bool:
	
	def solve(root):
		if not root:
			return True, 0
		if not root.left and not root.right:
			return True, root.data
		left,left_sum =solve(root.left)
		right,right_sum =solve(root.right)
		if left_sum!=float('inf') and right_sum!=float('inf') and left_sum+right_sum ==root.data:
			return True, root.data
		else:
			return False, float('inf')

	return solve(root)[0]

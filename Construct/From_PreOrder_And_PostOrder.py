## problem : construct BT from pre-order and post-order

#algorithm : to find the length of LST, and len(RST) = n- len(LST)

#recursively update the starting index of LST and RST and the number in the LST and RST

#until there is left one node in subtree, which is the base case of recursion, and return 

class Solution:

	def constructBinaryTree(self, preorder: List[int], postorder: List[int]) -> Node:
		
		def solve(i,j,n):
      #base case 1
			if n<=0:
				return None
        
			root =Node(preorder[i],None,None)
      
      ##base case 2
			if n==1: # return on leaf node, because no Subtree for a leaf
				return root
			
      #k is to find the length of LST 
			k=j
			while postorder[k]!=preorder[i+1]:
				k+=1
      
			l = k- j+1 
      
      #recursively update the Starting Point of pre-order index and post-order index in LST and RST
			root.left =solve(i+1, j, l)
      #same for RST
			root.right=solve(i+l+1, k+1, n-l-1)
			return root
      
		i=0
		j=0
		n=len(preorder)
		return solve(i,j,n)

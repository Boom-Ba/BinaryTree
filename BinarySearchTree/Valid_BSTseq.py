"""
Input : [15, 10, 8, 12, 20, 16, 25]
Output: True
Explanation: The following BST can be constructed from the above sequence and it has the same preorder traversal:

		  15
		/	 \
   /	  \
  /		   \
 10		   20
/  \	  /  \
 /	\	 /	  \
8		12	16	  25

"""

def isBST(self, seq: List[int]) -> bool:
    # check if each index satisfy the property of BST
		def Valid(seq, min_, max_, index):
			if index==len(seq): 
				return None, index
			
			val =seq[index]
			
			if val<min_ or val>max_:
				return None, index
				
			root=Node(val)
			
			index+=1 #move to nxt index 
			root.left, index =Valid(seq, min_, val, index)
			root.right,index=Valid(seq,val,max_,index)
    
			return root, index
		
		idx= 0 
		retIndex=Valid(seq,-sys.maxsize,sys.maxsize,0)[1]
		return retIndex ==len(seq)


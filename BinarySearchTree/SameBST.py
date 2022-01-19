"""
given two set of BST keys, X & Y. checck if these keys are belong to the same tree without constructing the BST
"""
class Solution:
	def isSameBSTs(self, X: List[int], Y: List[int]) -> bool:
		# Write your code here...
		
		def sameTree(n, X, Y) :
			#X=[] Y=[]
			if n==0:
				return True
				
			if X[0]!=Y[0]:
				return False
			
			if n==1:
				return True
				
			#create auxiliary array to store num in root.left, root.right
			LeftX=[None] * (n-1)
			RightX= [None]* (n-1)
			LeftY =[None] * (n-1)
			RightY=[None]*(n-1)
			
			l =m= j =k =0
			"""
			l is the index to store elements < X 's root
			m is the index to store elements > X 's root
			n is the index to store elements < Y 's root
			k is the index to store elements > Y 's root
			"""
			for i in range(1, n):
				#left elements in X
				if X[i] <X[0]:
					LeftX[l]  = X[i]
					l+=1
					
				else:
					RightX[m] = X[i]
					m+=1
				
				if Y[i]<Y[0]:
					LeftY[j] =Y[i]
					j+=1
				else:
					RightY[k] =Y[i]
					k+=1
			
			if l!=j or m!=k:
				return False
			return sameTree(l,LeftX,LeftY) and sameTree(m,RightX,RightY)
			
		
		return len(X)==len(Y) and sameTree(len(X),X,Y )

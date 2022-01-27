from collections import deque
class Solution:
    def minLeafSum(self,root):
        
        isleaf=0 
        
        if not root:
            return 0
        #level order traversal
        
        #notice: base case if only contains one root node
        if not root.left and not root.right:
            return root.data
            
        q= deque([root])
        sum_=0
        while isleaf==0: 
            #while haven't reachout to leaf
            #pop out current level will stop
            qSize =len(q)
            for _ in range(qSize):
                node= q.popleft()
                if node.left ==None and node.right==None: #isLeaf node
                    sum_+=node.data
                    isleaf=1 
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
        return sum_

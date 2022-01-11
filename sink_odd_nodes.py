#sink odd nodes in BT
#sink odd value node such no parent of subtree is odd-value

class Node:

  def__init__(self,val==None):
    self.val=val
    self.left=None
    self.right=None
  def isleaf(self, root):
    return (node.left==None and node.right==None )
  #if root node is odd value, sink the root
  def sink(self,root):
    #if not root or root is leaf, do nothing
    if root==None or isLeaf(root):
      return
    #if root has LST, and root.left has even value
    if root.left !=None and not root.left.val&1:
      root.val,root.left.val =root.left.val,root.val
      sink(root.left)
    elif root.right !=None and not root.right.val&1:
      root.val,root.right.val =root.right.val,root.val
      sink(root.right)

def sinkOddNodes(root):
  if root==None or root.isleaf()==True:
    return 
  
  #if root has LST and root.left is odd value
  if root.val&1:
    root.sink(root)
  sinkOddNodes(root.left)
  sinkOddNodes(root.right)
  

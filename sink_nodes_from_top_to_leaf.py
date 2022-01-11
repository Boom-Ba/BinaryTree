##SINK ALL 0 ELEMENTS INTO BOTTOM OF TREE
class Node:

  def __init__(self,val=None):
    self.val=val
    self.left=None
    self.right=None
def isLeaf(node):
  return (node.left==None and node.right==None)
##sink a node 
def sink(node):
  if not node or isLeaf(node):
    return
  #if node has left sub tree and node's left!=0
  if node.left !=None and not node.left.val ==0:
    node.left.val,node.val=node.val,node.left.val
    sink(node.left)
  elif node.right !=None and not node.right.val ==0:
    node.right.val,node.val=node.val,node.right.val
    sink(node.right)
#sink all 0s in BT
def sink_0(root):
  if not root:
    return 
  if root.val==0:
    sink(root)
  sink_0(root.left)
  sink_0(root.right)
  
  
##LNR
def inorder(root):
  if not root:
    return 
  inorder(root.left)
  print(root.val)
  inorder(root.right)
if __name__ == '__main__':
  root = Node(0)
  root.left = Node(1)
  root.right = Node(0)
  root.right.left = Node(0)
  root.right.right = Node(2)
  root.right.left.left = Node(3)
  root.right.left.right = Node(4)

  sink_0(root)
  inorder(root)

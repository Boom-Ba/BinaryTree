## Find lowest common ancestor 
##algorithm: check if both two nodes exsit, then find the LCA
class Node:
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right=None

def isPresent(root,node):
  if not root:
    return False
  if root==node:
    return True
  left =isPresent(root.left,node)
  right=isPresent(root.right,node)
  return left or right
  
def findLCA(root,lca, x,y):
  if not root:
    return False, lca
  if root==x or root==y:
    return True, root
  left, lca =findLCA(root.left,lca, x,y)
  right, lca = findLCA(root.right,lca, x,y)
  if left and right:
    lca=root
  return (left or right), lca 
if __name__=='__main__':
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  root.left.right = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)
  lca=None
  x=root.left.right.left
  y=root.right
  if not isPresent(root,x) or not isPresent(root,y)  :
    print('False')
  res=findLCA(root,lca,x,y)
  print(res)

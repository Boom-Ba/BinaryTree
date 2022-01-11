def swap(node):
  if node is None:
    return 
  node.left,node.right=node.right,node.left
##invert BT
def invert(root):
  if not root:
    return 
  if not root.left and not root.right:
    return 
  if root!=None:
    swap(root)
  invert(root.left)
  invert(root.right)

invert(root)

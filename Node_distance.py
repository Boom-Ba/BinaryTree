##distance between a pair of nodes
#1. find LCA 
#2. dist(x,LCA) + dist(y,LCA)
def find_level(root,node,level):
  if root is None:
    return -float('inf')
  if node==root:
    return level
  
  left = find_level(root.left, node, level+1)
  if left!=-float('inf'):
    return left
  return find_level(root.right, node, level + 1)

def isPresent(root,node):
  if not root:
    return False
  if node==root:
    return True
  left= isPresent(root.left,node)
  right =isPresent(root.right,node)
  return left or right

def LCA(root,x,y,lca=None):
  if root==x or root==y:
    return True,root
  left, lca = LCA(root.left,x,y,lca)

  right,lca=LCA(root.right,x,y,lca)
  if left and right:
    return True, root
  return (left or right) ,lca 

def find_distance(root,x,y):
  lca=None
  if not isPresent(root,x) or not isPresent(root,y):
    return -1
  
  lca_n=LCA(root,x,y,lca)[1]
  return find_level(lca_n,x,0)+find_level(lca_n,y,0)
  

if __name__=='__main__':
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  root.left.right = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)
 
  x=root.left
  y=root.right
  d= find_distance(root,x,y)
  print(d)
  #found lca
  
  
  """
           1
        2.    3
          4  5  6 
            7  8
  """

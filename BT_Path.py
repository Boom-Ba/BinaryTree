class Node:
  def __init__(self,val=None):
    self.left=None
    self.right=None
    self.val=val

## calculate binary value path sum in BT
def Binary_path_sum(curr,s):
  global a
  if not curr:
      return 0
  #base case one node
  if not curr.left and not curr.right:
      s+=str(curr.val)
      a+=int(s,2)
      return  
  s+=str(curr.val)
  if curr.left:
    Binary_path_sum(curr.left,s)
  if curr.right:
    Binary_path_sum(curr.right,s)

#print the path from Tree's top -> bottom in string format
def print_path_top_to_bottom(node,s,ret):
  if not node:
    return ''
  #base case one node
  if not node.left and not node.right:
    #add node.val to str
    s+=str(node.val)
    print(s)
  s+=str(node.val)
  print_path_top_to_bottom(node.left,s)
  print_path_top_to_bottom(node.right,s)
#Sum node's value from Top to bottom
def pathSum(node,ans):
  if not node:
    return 0
  if not node.left and not node.right:
    ans+=node.val
    print(ans)
  ans+=node.val
  pathSum(node.left,ans)
  pathSum(node.right,ans)
#Binary Sum from Top to Bottom

if __name__== '__main__':
  root=Node(1)
  root.left=Node(0)
  root.left.left=Node(0)
  root.left.right=Node(1)
  root.right =Node(1)
  root.right.left=Node(0)
  root.right.right=Node(1)
   
  # print_path_top_to_bottom(root,'')
  # pathSum(root,0)
  
  a=0
  Binary_path_sum(root,'')
  print(a)

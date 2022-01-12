##output: ABB LB, .. 

digits =[1,2,2]
class Node:
  def __init__(self,key='',left=None,right=None):
    self.key=key
    self.left=None
    self.right=None
def printT(node):
  if not node:
    return 
  if not node.left and not node.right:
    print(node.key)
  printT(node.right) ##right is single char concatenation 
  printT(node.left) #left is 2-digits 
def construct(root, map,digits,i):
  if not root or i ==len(digits):
    return
  
  if i+1<len(digits):
    t =10*digits[i]+digits[i+1]

    if t<=26:
      root.left= Node(root.key+map[t-1])
      construct(root.left, map, digits,i+2)
  root.right=Node(root.key+map[digits[i]-1])
  construct(root.right,map,digits,i+1)
root=Node()
map ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
construct(root, map,digits,0)
printT(root)

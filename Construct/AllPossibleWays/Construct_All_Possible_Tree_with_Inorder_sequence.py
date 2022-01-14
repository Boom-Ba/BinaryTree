# Find all possible binary trees having the same inorder traversal

# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
 
 
# def preorder(root):
#     if root is None:
#         return
#     print(root.data, end=' ')
#     preorder(root.left)
#     preorder(root.right)

##generating all trees with same inorder sequence
#can get 5 trees 
def construct(inorder, start, end):
  trees= []
  if start>end:
    trees.append(None)
    return trees

  for idx in range(start,end+1): #include end node
    curr_root=None
    LST= construct(inorder, start, idx-1) 
    RST= construct(inorder, idx+1, end)
   
    for l in LST:
      for r in RST:
      #form a tree with inorder[idx] as root_node, and l, r subtree
        curr_root =Node(inorder[idx],l,r)
        trees.append(curr_root)
    
  return trees
##verify if their inorder results are all same 
def traverse(tree,curr):
  if not tree:
    return 
  
  traverse(tree.left,curr)
  curr.append(tree.data)
  traverse(tree.right,curr)

if __name__=='__main__':
  ##inorder: left, root, right
  inorder= [1,2,3]
  
  trees=construct(inorder, 0, 2)
  ret=[]
  #if print out all in-order sequences, all 5 tress are same 
  for t in trees:
    cur=[]
    traverse(t,cur)
    print(cur)
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
